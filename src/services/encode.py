import time

import hashlib


class Encoding:

    @staticmethod
    def encode_language(text):
        result = hashlib.sha1(text.encode())
        return result.hexdigest()

    @staticmethod
    def process_languages(object_text):
        start_time = time.time()
        language = encode_language(object_text[0]['name'])

        return '{}/{}'.format(language, str(round(time.time() - start_time, 3)))
