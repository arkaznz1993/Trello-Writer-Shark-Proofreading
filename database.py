import os
import mysql.connector
from mysql.connector.constants import ClientFlag

# Instance name - flash-hour-338103:asia-south1:test-sql-server

config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': '35.200.140.194',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': os.environ.get('SSL_CA'),
    'ssl_cert': os.environ.get('SSL_CERT'),
    'ssl_key': os.environ.get('SSL_KEY'),
    'database': os.environ.get('DB_NAME'),
}

GET_CUSTOM_FIELDS = 'SELECT * FROM CustomFields;'

GET_CUSTOM_FIELD_OPTIONS = 'SELECT CustomFieldOptions.* FROM CustomFieldOptions ' \
                           'JOIN CustomFields ON CustomFieldOptions.IdCustomField = CustomFields.Id;'

INSERT_CARD = 'INSERT INTO CardDetails (' \
              'CardId, CardTitle, CardUrl, Type, Priority,' \
              'MaxWordCount, WordCount, Multiplier,' \
              'Client, Writer, Team, SubmittedDate,' \
              'SurferSEOLink, OriginalDocLink, FirstDocLink, Status)' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ' \
              'ON DUPLICATE KEY UPDATE ' \
              'CardTitle = VALUES(CardTitle),' \
              'CardUrl = VALUES(CardUrl),' \
              'Type = VALUES(Type),' \
              'Priority = VALUES(Priority),' \
              'MaxWordCount = VALUES(MaxWordCount),' \
              'WordCount = VALUES(WordCount),' \
              'Multiplier = VALUES(Multiplier),' \
              'Client = VALUES(Client),' \
              'Writer = VALUES(Writer),' \
              'Team = VALUES(Team),' \
              'SubmittedDate = VALUES(SubmittedDate),' \
              'SurferSEOLink = VALUES(SurferSEOLink),' \
              'OriginalDocLink = VALUES(OriginalDocLink),' \
              'FirstDocLink = VALUES(FirstDocLink),' \
              'Status = VALUES(Status);'


class DatabaseConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def get_custom_fields(self):
        self.cursor.execute(GET_CUSTOM_FIELDS)
        return self.cursor.fetchall()

    def get_custom_field_options(self):
        self.cursor.execute(GET_CUSTOM_FIELD_OPTIONS)
        return self.cursor.fetchall()

    def insert_card_details(self, cards: list):
        values = []
        for card in cards:
            values.append(card.convert_to_tuple_proofreading())
        self.cursor.executemany(INSERT_CARD, values)
        self.connection.commit()
