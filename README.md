# Task 1
Create a script that recursively downloads a given webpage and finds all hyperlink in that
webpage. It should then explore all the hyperlinks and carry doing that in a recursive way. In
each of this recursive crawling, it finds all the appearance of the given search word and
displays them.
Create the script that takes in parameters while execution in the format:
Format: ./script.sh “website_address” “search_word”
Example: ./script.sh www.usec.io Ninja

# Solution
I have created a solution using Python instead in task_1.py
I have assumed that the requested keywords should be part of the links or their related titles. 
Also a visited link should not be crawled again

# Task 2
Write a socket server program that listens on port 2999. Through this socket program you are able to
execute the script that you wrote in Problem 1 of Shell Programming Questions. Make this socket
server program a system service which can be controlled by systemctl (like start, stop and restart
this socket server). Also write a client socket program for testing it. (In other words, by using a test
client program in running on one computer, a user is able to connect to another computer socket
and execute the script on it.)

# Solution
To create a system service copy the task_2.service in
`/etc/systemd/system/task_2.service`

adapt the correct paths in it and then run
`systemctl daemon-reload && systemctl enable task_2 && systemctl start task_2 --no-block`

Test-run it with
`python3 task_2_client.py`

# Task 3
For task_3 I have used python 2.7 due to problems with the newer versions of Django and Channels
The task is not 100% complete, but the data is visible and the sockets are up. I was not able to automate the 
visualization, but it is around 95% complete.

To install it run `pip install -r requirements.txt` and then `python manage.py mgirate && python manage.py runserver`
The new data is added in the admin panel and is visualizing on `http://localhost:8000/temperature`

# Task 4
My view on the theoritical task is in the file of task_4.txt