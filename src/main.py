from socket_client import SocketClient
from prompt_toolkit import PromptSession

TIMEOUT_SECONDS = 10

def main():
    client = SocketClient(TIMEOUT_SECONDS)
    session = PromptSession()
    """
     Improvements which can be made: 
     1. Validate search string for invalid chars, min / max length and return an error without making a socket call
     2. Add a progress bar to indicate the user to wait / provide some visual feedback
     3. Explore async api, see if rows can be fetched async and then ordered and returned 
    """
    print("Welcome to the StarWars client!")

    while True:
        try:
            text = session.prompt('> Search your favorite characters:')
            print(f'You entered: {text}, response is below:')
            client.search(text)
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        except Exception as e: # handles any connection / unexpected errors
            print(f"Unexpected error: {e}, try again!")

    print('Exiting Search CLI!')

if __name__ == "__main__":
    main()
