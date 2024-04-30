Steps to run `main.py`

Prerequisites:
- Make sure Python is installed. Typing `python` in the terminal should work, and verify that Python version is >= 3.9.6. 
  **Note**: May also work with older Python versions but I haven't tested it with older versions.

- Start the API server by running `docker run -p 3000:3000 clonardo/socketio-backend`

Steps:
- go to the project root on your command line 
- Install the deps using `python -m pip install -r requirements.txt`
- Then run `python src/main.py`