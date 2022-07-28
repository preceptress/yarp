# updates.py
import praw
import psycopg2


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def bad_request(message):
    return error_response(400, message)

reddit = praw.Reddit(client_id='abcdefghijklmnopqrstuvwxyz',
                     client_secret='abcdefghijklmnopqrstuvwxyz',
                     user_agent='my user agent',
                     thing_limit=100)

# try to connect
try:
    connection = psycopg2.connect(
        "dbname='mydb' user='myuser' password='abcdefghijklmnopqrstuvwxyz'")
except:
    print("Error: Unable to connect to database.")

# sucess
cursor = connection.cursor()

def update():

    # loop through our Subreddit choices
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
                    '''INSERT INTO submissions(title,subreddit,permalink,url,utc,comments,score) VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT(permalink) DO NOTHING''', (my_title, j, my_permalink, my_url, my_utc, my_num_comments, my_score))
                connection.commit()

            except (Exception, psycopg2.Error) as error:
                if(connection):
                    print("Failed to insert record into table", error)
            finally:
                print("Success. Record Inserted or Ignored if duplicate")

            print(j)


# INIT update
update()

# FINISHED
connection.close()

print('UPDATE COMPLETED')

