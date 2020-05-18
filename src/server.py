from flask import Flask, request, Response, jsonify
import json
import os
import re

import pandas as pd
import requests

from src.services.encode import Encoding
from src.model.SQLite3 import HandleSQL


class HandleRegions:
    REGIONS = os.environ['regions']
    API_BY_REGION = 'https://restcountries.eu/rest/v2/region'

    def __init__(self):
        self.encode_handle = Encoding
        self.sqlite_handle = HandleSQL
        self.df_data = self.process()

        self.df_data = self.get_language_and_time(self.df_data)
        self.save_to_json(self.df_data)
        self.save_in_sqlite(self.df_data)

    def process(self):
        df_regions_cities = pd.DataFrame()

        for region in self.REGIONS:
            response = requests.get(
                '{}/{}'.format(self.API_BY_REGION, region))

            json_data = json.loads(response.text)

            df_regions_cities = df_regions_cities.append(
                pd.DataFrame.from_dict(json_data)[
                    ['name', 'region', 'languages']]
            )

        return df_regions_cities

    def get_language_and_time(self, df_data):
        df_data['language'] = df_data['languages'].apply(
            self.encode_handle.process_languages)
        df_data[['language', 'time']] = df_data['language'].str.split(
            '/', expand=True)
        df_data.drop(columns=['languages'], inplace=True)

        print('Valor minimo ', df_data['time'].min())
        print('Valor maximo ', df_data['time'].max())
        print('Valor promedio ', df_data['time'].mean())
        print('Valor total ', df_data['time'].sum())
        return df_data

    def save_to_json(self, df_data):
        df_data.to_json(
            orient='records', path_or_buf='data.json')

    def save_in_sqlite(self, df_data):
        self.sqlite_handle.sql_insert(df_data)
