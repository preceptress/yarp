# updates.py
# import requests

import os
import praw
import psycopg2

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def bad_request(message):
    return error_response(400, message)

# connect with praw pass credationals
reddit = praw.Reddit(client_id=os.getenv('client_id'),client_secret=os.getenv('client_secret'),user_agent=os.getenv('user_agent'),thing_limit=os.getenv('thing_limit'))

# try to connect
conn_string = "dbname=%s user=%s password=%s" % (os.getenv('db_name'),os.getenv('db_user'), os.getenv('db_password'))
connection = psycopg2.connect(conn_string)

# sucess
cursor = connection.cursor()

def update():

    # loop through our choices
    choicesArray = ["reddit",
                    "funny",
                    "AskReddit",
                    "gaming",
                    "aww",
                    "Music",
                    "pics",
                    "science",
                    "worldnews"]

    for j in choicesArray:

        for submission in reddit.subreddit(j).new(limit=3):
            my_title = submission.title
            my_permalink = "https://www.reddit.com" + submission.permalink
            my_url = submission.url
            my_utc = submission.created_utc
            my_num_comments = submission.num_comments
            my_score = submission.score

            try:
                cursor.execute(
                    '''INSERT INTO submissions(title,subreddit,permalink,url,utc,comments,score) VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING''', (my_title, j, my_permalink, my_url, my_utc, my_num_comments, my_score))
                connection.commit()

            except (Exception, psycopg2.Error) as error:
                if(connection):
                    print("Failed to insert record into mobile table", error)
            finally:
                print("Sucess! Record was added  or ignored if duplicate")

            print(j)

# INIT update
update()

# FINISHED
connection.close()

print('UPDATE COMPLETED')

