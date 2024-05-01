import os

from socket_client import SocketClient
from prompt_toolkit import PromptSession

CLIENT_TIMEOUT_SECONDS = 10

def main():
    star_wars_client = SocketClient(CLIENT_TIMEOUT_SECONDS)
    session = PromptSession()
    """
     Improvements which can be made: 
     1. Validate search string for invalid chars, min / max length and return an error without making a socket call
     2. Add a progress bar to indicate the user to wait / provide some visual feedback
     3. Explore async api, see if rows can be fetched async and then ordered and returned
     4. Add code to recognize 'exit()' string and exit the CLI.
     5. Add Integration tests 
    """
    print("Welcome to StarWars Search CLI: You will find only what you bring in!")

    while True:
        try:
            text = session.prompt('> Search your favorite characters:')
            if text == "exit()":
                break

            print(f'Searching for names containing: "{text}" {os.linesep}')
            star_wars_client.search(text)

        except KeyboardInterrupt:
            break

        except Exception as e: # handles any connection / unexpected errors
            print(f"Unexpected error: {e}, maybe search again!")

    print('Exiting StarWars CLI -> Feel the force!')

if __name__ == "__main__":
    main()
