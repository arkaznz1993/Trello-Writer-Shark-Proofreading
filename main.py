import requests
import constants
from card import Card
from google_service import google_service
from database import DatabaseConnector
import time
from holiday import holiday

completed_list_ids = ['61eba09d4e95bb2b66dae705', '61eba0f9cf78456e54912062']


def main():
    time_start = time.time()
    if not holiday:
        database_connection = DatabaseConnector()
        Card.docs_service = google_service(constants.DOCS)
        Card.drive_service = google_service(constants.DRIVE)

        for list_id in completed_list_ids:
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

        for card in Card.all_cards:
            card.move_card_to_ready()

    time_end = time.time()
    print(f'Time taken for program: {int(time_end - time_start)} seconds.')


if __name__ == '__main__':
    main()