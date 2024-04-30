Steps to run `main.py`

**Prerequisites:**
- Start the API server by running `docker run -p 3000:3000 clonardo/socketio-backend`
- Make sure Python is installed. Typing `python' in the terminal should work, and verify that Python version is >= 3.9.6. 
- **Note 1**: May also work with older Python versions but I haven't tested it with older versions.
- **Note 2**: Some systems may have Python installed as `python3`, so see if that works. In which case replace 'python' with `python3` in the commands shown below.

**Steps:**
- Go to the project root on your command line. 
- Install the deps using `python -m pip install -r requirements.txt`.
- Then run `python src/main.py`.