import os

from socket_client import SocketClient
from prompt_toolkit import PromptSession

# adjust this timeout to get a quicker error response upon API server unavailability
CLIENT_TIMEOUT_SECONDS = 10
HOST_URL = 'http://localhost:3000'

"""
     Improvements which can be made: 
     1. Validate search string for invalid chars, min / max length and return an error without making a socket call
     2. Add a progress bar to indicate the user to wait / provide some visual feedback
     3. Explore async api, see if rows can be fetched async and then ordered and returned
     4. Add Integration tests 
    """


def main():
    star_wars_client = SocketClient(HOST_URL, CLIENT_TIMEOUT_SECONDS)
    session = PromptSession()

    print(f"{os.linesep}>>>>Welcome to StarWars Search CLI: You will find only what you bring in! <<<<{os.linesep}")
    print(f"Note: To exit from the CLI, type 'exit()'")

    # start the CLI loop
    while True:
        try:
            text = session.prompt(f'{os.linesep}<!> Search your favorite characters:')
            if text == "exit()":
                break

            print(f'{os.linesep}Searching for names containing: "{text}" {os.linesep}')
            star_wars_client.search(text)

        except KeyboardInterrupt:
            break

        except Exception as e:  # handles any connection / unexpected errors
            print(f"Unexpected error: {e}, maybe search again!")

    print(f'{os.linesep}=====> Exiting StarWars CLI -> You felt the force!! <=====')


if __name__ == "__main__":
    main()
