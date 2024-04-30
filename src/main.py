from socket_client import SocketClient
from prompt_toolkit import PromptSession

MAX_INPUT_LENGTH = 25


def main():
    client = SocketClient()
    session = PromptSession()
    """
     Improvements: 
     1. Validate search string for invalid chars, min / max length and return an error without making a socket call
     2. Add a progress bar to indicate the user to wait / provide some visual feedback
     3. Explore async api, see if rows can be fetched async and then ordered and returned
     4. Handle API server unavailability, 
        scenarios: 
            a: Stopping the dcoker instance in the middle of receiving responses for a query
            b. Server is unavailble from the get-go 
    """

    while True:
        try:
            text = session.prompt('> Enter your search text:')
            print(f'You entered: {text}, response is below:')
            client.search(text)
        except KeyboardInterrupt:
            break
        except EOFError:
            break

    print('Done!')

if __name__ == "__main__":
    main()
