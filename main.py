import requests
import constants
from card import Card
from custom_field import CustomField
from custom_field_options import CustomFieldOption
from google_service import google_service
from database import DatabaseConnector
import time
from holiday import holiday


def main(data, context):
    time_start = time.time()
    if not holiday:
        database_connection = DatabaseConnector()
        Card.docs_service = google_service(constants.DOCS)
        Card.drive_service = google_service(constants.DRIVE)
        CustomField.instantiate_from_list(database_connection.get_custom_fields())
        CustomFieldOption.instantiate_from_list(database_connection.get_custom_field_options())

        for list_id in constants.COMPLETED_LIST_IDS:
            url = f"https://api.trello.com/1/lists/{list_id}/cards"

            response = requests.request(
                "GET",
                url,
                params=constants.PARAMS,
                headers=constants.HEADERS
            )

            Card.instantiate_from_json(response.json())

        database_connection.insert_card_details(Card.all_cards)
        database_connection.connection.close()

        Card.move_cards_to_ready()

    time_end = time.time()
    print(f'Time taken for program: {int(time_end - time_start)} seconds.')


if __name__ == '__main__':
    main('', '')
