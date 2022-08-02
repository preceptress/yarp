# YARP
### The YARP Engine. Yet Another Realtime Parser.

There is a lot of cool information on Reddit - but sometimes it can get buried. 
Google Search is overwhelming, a tsunami of info. The default Reddit search can take you down a very deep rabbit hole. And still not find what you are lookinkg for.

The solution: YARP. Yet Another Realtime Parser.

Open Source. Super Fast. Like the speed of light (allmost) kind of fast. If you are doing anything with the Reddit API you will need a database at one point.  This is a starting point. Easy to modify for your projects.

You do need to register your App with Reddit to get a App ID and Secret Key. All your constants are stored in a local .env file.

https://www.reddit.com/prefs/apps/

The heart of YARP: The Postgres Data Dictonary and how to levearge the tsvector filed for searching. You also will need to create a PostgresSQL trigger. A link to understand how this is implemented.

https://hamon.in/blog/sqlalchemy-and-full-text-searching-in-postgresql

![alt text](https://user-images.githubusercontent.com/105808631/181388037-01a5acfd-1b89-4da7-b38f-bd452c48a59d.png)

You can se up YARP as a Cron job, I've found that every 5 mins seems to work well. The default code makes an assumption that no subreddit dds 12 new Origitnal posts ain 5 mins. So far that seems to be holding. If you have a supewr active subreddit, you may have to adust that value. 


*/5 * * * * /home/my_user/app/venv/bin/python /home/my_user/app/update.py

Score and Comments are for demo purposes to show how to capture values since we are looking at 5 min intervals and only New Records they are only valid for the time we indexed the record.

Subreddit data saved to PoatgresSQL.

![alt text](https://user-images.githubusercontent.com/105808631/181680969-a60c94df-3dfc-4841-9b97-ade10c7beb95.png)

Resources for lists of Reddit subreddits:

http://redditlist.com/

https://blog.oneupapp.io/biggest-subreddits/

https://www.reddit.com/subreddits/leaderboard/

Using the YARP engine for real time (or close too) Covid news from Reddit:


![alt text](https://user-images.githubusercontent.com/105808631/182400732-89ea2223-a554-453e-a886-26d2bc1a4144.png)



