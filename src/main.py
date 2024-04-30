from src.socket_client import SocketClient
from prompt_toolkit import PromptSession

MAX_INPUT_LENGTH = 25


def main():
    client = SocketClient()
    session = PromptSession()
    """
     TODOs: 
     1. check for empty string and return an error without making a socket call
     2. max user input string length validation
     3. add a progress bar to indicate the user to wait / provide some visual feedback
     4. make it async, see if rows can be fetched async and then ordered and returned
    """

    while True:
        try:
            text = session.prompt('> ')
            print(f'You entered: {text}, response is below:')
            client.search(text)
        except KeyboardInterrupt:
            break
        except EOFError:
            break

    print('Done!')


if __name__ == "__main__":
    main()
