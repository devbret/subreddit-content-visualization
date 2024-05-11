# Interactive Subreddit Word Cloud

![Preview Of Resulting Visualization](https://hosting.photobucket.com/images/i/bernhoftbret/programming-subreddit-word-cloud.jpg)

Visualize popular phrases from recent content on various subreddits as an interactive word cloud, using Python and D3.

If you would like to view a demo of this program, here is [a YouTube video](https://youtu.be/xsDcf0VjNgU) you might find useful.

## Set Up

### Programs Needed 

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) (When installing on Windows, make sure you check the ["Add python 3.xx to PATH"](https://hosting.photobucket.com/images/i/bernhoftbret/python.png) box.)

### Steps

1. Install the above programs.
2. Open a shell window (For Windows open PowerShell, for MacOS open Terminal & for Linux open your distro's terminal emulator).
3. Clone this repository using `git` by running the following command; `git clone https://github.com/devbret/subreddit-content-visualization`.
4. Navigate to the repo's directory by running; `cd subreddit-content-visualization`.
5. Install the needed dependencies for running the script by running; `pip install -r requirements.txt`.
6. Open and edit the app.py file (in an editor of your choice) on line 11, to include the subreddits that you would like to visualize as a word cloud.
7. Run the script with the command `python3 app.py`.
8. To view the data with the index.html file, you will need to run a local web server. To do this run `python3 -m http.server`.
