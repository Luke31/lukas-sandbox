ES_TYPE_NAME = 'email'

SUPPORTED_LANG_CODES_ANALYZERS = {'ja': 'kuromoji',
                                  'en': 'english',
                                  'un': 'standard'}
FALLBACK_LANG_CODE = 'un'
JA_USER_DICT = 'userdict_ja.txt'  # /etc/elasticsearch/userdict_ja.txt
ES_BULK_CHUNK_SIZE = 2000