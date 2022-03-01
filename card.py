import re
from datetime import datetime
import requests
import constants
from custom_field import CustomField
from custom_field_options import CustomFieldOption
from docs import Docs
from google_service import get_id_from_url

URL = "https://api.trello.com/1/cards"
STATUS_PROOFREADING = 1


class Card:
    all_cards = []
    docs_service = None
    drive_service = None

    def __init__(self, id: str, title: str, url: str, id_list: str, id_board: str, desc: str):
        self.id = id
        self.title = title
        self.url = url
        self.id_list = id_list
        self.id_board = id_board
        self.desc = desc
        self.writer = None
        self.team = None
        self.proofreader = None
        self.max_word_count = 6000
        self.word_count = None
        self.multiplier = 1
        self.client = 1
        self.type = None
        self.priority = None
        self.persona = None
        self.surfer_seo = None
        self.doc_file_original = ''
        self.doc_file_copy1 = None
        self.submitted_date = None
        self.status = STATUS_PROOFREADING
        self.remarks = 'None'

        try:
            if self.id_board == constants.BOARD_ID_TEAM_ALPHA:
                self.team = 'Team Alpha'
            elif self.id_board == constants.BOARD_ID_TEAM_BETA:
                self.team = 'Team Beta'

            max_word_count_string = re.findall(pattern=constants.MAX_WORD_COUNT_PATTERN, string=self.title)[0]
            self.max_word_count = int(max_word_count_string.split(' ')[0])
            self.set_card_writer()
            self.set_card_custom_fields()
            self.get_card_doc_link()

            if self.doc_file_original.startswith('https://docs.google.com/document/d/'):
                doc_id = get_id_from_url(self.doc_file_original)
                doc_file = Docs(Card.docs_service, doc_id)

                self.word_count = doc_file.word_count
                if self.word_count > self.max_word_count:
                    self.word_count = self.max_word_count

                copy_title = doc_file.title
                body = {
                    'name': copy_title
                }
                drive_response = Card.drive_service.files().copy(
                    fileId=doc_id, body=body).execute()
                document_copy_id = drive_response.get('id')
                self.doc_file_copy1 = constants.GOOGLE_DOC_LINK.replace('[DOC_ID]', document_copy_id)
            else:
                self.word_count = self.max_word_count
                self.doc_file_copy1 = self.doc_file_original

            Card.all_cards.append(self)
        except:
            pass

    @staticmethod
    def instantiate_from_json(cards_json):
        for card_json in cards_json:
            Card(
                card_json['id'],
                card_json['name'],
                card_json['url'],
                card_json['idList'],
                card_json['idBoard'],
                card_json['desc']
            )

    def set_card_writer(self):
        actions_url = URL + f'/{self.id}/actions'
        params = constants.PARAMS.copy()
        params["filter"] = "addMemberToCard"
        response = requests.request(
            "GET",
            actions_url,
            params=params,
            headers=constants.HEADERS
        )

        card_members_json = response.json()
        self.writer = card_members_json[0]['data']['member']['id']

    def set_card_custom_fields(self):
        proofreading_field_url = URL + f'/{self.id}/customFieldItems'

        response = requests.request(
            "GET",
            proofreading_field_url,
            params=constants.PARAMS,
            headers=constants.HEADERS
        )

        now = datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        self.submitted_date = now

        for custom_field_json in response.json():
            c_field = CustomField.get_custom_field_by_id(custom_field_json['idCustomField'])
            if c_field is not None:
                if c_field.name == 'Type':
                    cfo = CustomFieldOption.get_custom_field_option_by_id(custom_field_json['idValue'])
                    self.type = cfo.field_value
                    print(self.type)
                elif c_field.name == 'Priority':
                    cfo = CustomFieldOption.get_custom_field_option_by_id(custom_field_json['idValue'])
                    self.priority = cfo.field_value
                    print(self.priority)
                elif c_field.name == 'Persona':
                    cfo = CustomFieldOption.get_custom_field_option_by_id(custom_field_json['idValue'])
                    self.persona = cfo.field_value
                    print(self.persona)
                elif c_field.name == 'Surfer SEO':
                    self.surfer_seo = custom_field_json['value']['text']
                    print(self.surfer_seo)
                elif c_field.name == 'Client ID':
                    self.client = custom_field_json['value']['number']
                    print(self.client)
                elif c_field.name == 'Multiplier':
                    self.multiplier = custom_field_json['value']['number']
                    print(self.multiplier)

    def get_card_doc_link(self):
        actions_url = URL + f'/{self.id}/actions'
        params = constants.PARAMS.copy()
        params["filter"] = "commentCard"
        response = requests.request(
            "GET",
            actions_url,
            params=params,
            headers=constants.HEADERS
        )
        doc_link = ''
        for comment_json in response.json():
            try:
                comment_text = comment_json['data']['text']
                if comment_text.startswith('https://docs.google.com/document/d/'):
                    doc_link = comment_text
            except:
                print('Ran into an error.')

        if len(doc_link) > 0:
            self.doc_file_original = doc_link
        else:
            self.doc_file_original = self.surfer_seo

    def convert_to_tuple_proofreading(self):
        return (
            self.id, self.title, self.url, self.type, self.priority, self.max_word_count, self.word_count,
            self.multiplier, self.client, self.writer, self.team, self.submitted_date, self.surfer_seo,
            self.doc_file_original, self.doc_file_copy1, self.status)

    @staticmethod
    def move_cards_to_ready():
        for card in Card.all_cards:
            update_url = URL + f'/{card.id}/'
            params = constants.PARAMS.copy()
            if card.team == 'Team Alpha':
                params['idBoard'] = constants.BOARD_ID_EDITOR_ALPHA
                params['idList'] = constants.PROOFREADING_LIST_EDITOR_ALPHA
            elif card.team == 'Team Beta':
                params['idBoard'] = constants.BOARD_ID_EDITOR_BETA
                params['idList'] = constants.PROOFREADING_LIST_EDITOR_BETA
            else:
                # Add Team Gamma details later
                pass

            response = requests.request(
                "PUT",
                update_url,
                params=params,
                headers=constants.HEADERS
            )

            print(response.status_code)
