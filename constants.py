import os

GOOGLE_DOC_LINK = 'https://docs.google.com/document/d/[DOC_ID]/edit'


API_KEY = os.environ.get("TRELLO_API_KEY")
AUTH_TOKEN = os.environ.get("TRELLO_TOKEN")
PARAMS = {
    "key": API_KEY,
    "token": AUTH_TOKEN,
}
HEADERS = {
    "Accept": "application/json"
}

TYPE = 1
PRIORITY = 2
PERSONA = 3
SURFER_SEO = 4
CLIENT_ID = 5
MULTIPLIER = 6

MAX_WORD_COUNT_PATTERN = '[0-9]{3,5} words'

BOARD_ID_TEAM_1 = '6191c991ee98d37c936d4099'
BOARD_ID_TEAM_2 = '61eba0d2c21c0c191f4d021e'

VALUE_FIELDS_TEAM_1 = {
    '61e3a172cccf0404558256d1': TYPE,
    '61e3a172cccf0404558256e5': PRIORITY,
    '61e3a172cccf0404558256df': PERSONA,
    '61e64c337705ea0651a89fdc': SURFER_SEO,
    '61eba00daf37f450c4df38d4': CLIENT_ID,
    '62031fac15705a4d619bcc6a': MULTIPLIER
}

TYPE_VALUES_TEAM_1 = {
    '61e3a172cccf0404558256d2': 'Brand Pages',
    '61e3a172cccf0404558256d3': 'Product Reviews',
    '61e3a172cccf0404558256d4': 'Listicles',
    '61e3a172cccf0404558256d5': 'Website Content',
    '61e3a172cccf0404558256d6': 'Informational',
    '620320dd279a032bd92dd086': 'Sponsored',
    '620320e4a1ebea6600d05f50': 'Product Add On'
}

PRIORITY_VALUES_TEAM_1 = {
    '61e3a172cccf0404558256e6': 'Highest',
    '61e3a172cccf0404558256e7': 'High',
    '61e3a172cccf0404558256e8': 'Medium',
    '61e3a172cccf0404558256e9': 'Low',
}

PERSONA_VALUES_TEAM_1 = {
    '61e3a172cccf0404558256e0': 'Yes',
    '61e3a172cccf0404558256e1': 'No'
}

VALUE_FIELDS_TEAM_2 = {
    '61ed0b227920785203881777': TYPE,
    '61ed0b22792078520388178b': PRIORITY,
    '61ed0b227920785203881785': PERSONA,
    '61ed0b22792078520388176d': SURFER_SEO,
    '61ed0b22792078520388176a': CLIENT_ID,
    '62032538586fae8af6b3eba6': MULTIPLIER
}

TYPE_VALUES_TEAM_2 = {
    '61ed0b227920785203881778': 'Brand Pages',
    '61ed0b227920785203881779': 'Product Reviews',
    '61ed0b22792078520388177a': 'Listicles',
    '61ed0b22792078520388177b': 'Website Content',
    '61ed0b22792078520388177c': 'Informational',
    '62032538586fae8af6b3eba9': 'Sponsored',
    '620325f61d6e0f4c8a9eeea3': 'Product Add On'
}

PRIORITY_VALUES_TEAM_2 = {
    '61ed0b22792078520388178c': 'Highest',
    '61ed0b22792078520388178d': 'High',
    '61ed0b22792078520388178e': 'Medium',
    '61ed0b22792078520388178f': 'Low',
}

PERSONA_VALUES_TEAM_2 = {
    '61ed0b227920785203881786': 'Yes',
    '61ed0b227920785203881787': 'No'
}

# Service type constants for Google Services
SHEETS = 1
DOCS = 2
DRIVE = 3

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/gmail.send']

# Date Time Related Things
DATE_FORMAT = '%Y-%m-%d'
