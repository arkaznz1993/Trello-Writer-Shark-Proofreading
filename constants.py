import os

GOOGLE_DOC_LINK = 'https://docs.google.com/document/d/[DOC_ID]/edit'
USER_EMAIL = 'editor@writershark.com'

API_KEY = os.environ.get("TRELLO_API_KEY")
AUTH_TOKEN = os.environ.get("TRELLO_TOKEN")
PARAMS = {
    "key": API_KEY,
    "token": AUTH_TOKEN,
}
HEADERS = {
    "Accept": "application/json"
}

MAX_WORD_COUNT_PATTERN = '[0-9]{3,5} words'

COMPLETED_LIST_IDS = ['61eba09d4e95bb2b66dae705', '61eba0f9cf78456e54912062', '6221b3d250fffc5f461ed916']

BOARD_ID_TEAM_ALPHA = '6191c991ee98d37c936d4099'
BOARD_ID_TEAM_BETA = '61eba0d2c21c0c191f4d021e'
BOARD_ID_TEAM_GAMMA = '6221b38f6537a14b6aebd444'

BOARD_ID_EDITOR_ALPHA = '619c71771deda242e027685e'
PROOFREADING_LIST_EDITOR_ALPHA = '61e819cda4422b71873dd7f7'
BOARD_ID_EDITOR_BETA = '61ed0fd94bf5051e2602d02c'
PROOFREADING_LIST_EDITOR_BETA = '61ed0fe3d70a94477f001b6e'
BOARD_ID_EDITOR_GAMMA = '6221be34bd02aa64b89f82a2'
PROOFREADING_LIST_EDITOR_GAMMA = '6221be3b03f6b94f22314699'

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
