# YARP
### The YARP Engine. Yet Another Realtime Parser.

There is a lot of cool information on Reddit - but sometimes it can get buried. 
Google Search is overwhelming, a tsunami of info. The default Reddit search can take you down a rabbit hole of rabbits holes. And still not find what you are lookinkg for.

The engine: YARP. Yet Another Realtime Parser.

Open Source. Super Fast. Like the speed of light (allmost) kind of fast. If you are doing anything with the Reddit API you will need a database at one point.  This is a starting point. Easy to modify for your own projects.

You do need to register your App with Reddit to get a App ID and Secret Key. All your constants are stored in a local .env file.

https://www.reddit.com/prefs/apps/

Postgres Data Dictonary. The most interesting part is creating the tsvector field type for searching. You also will need to create a PostgresSQL trigger. This is a good link to understand how this is implemented.

https://hamon.in/blog/sqlalchemy-and-full-text-searching-in-postgresql

![alt text](https://user-images.githubusercontent.com/105808631/181388037-01a5acfd-1b89-4da7-b38f-bd452c48a59d.png)

You can set this up as a Cron job, I've found that every 5 mins seems to work well.


*/5 * * * * /home/my_user/app/venv/bin/python /home/my_user/app/update.py

Score and Comments are for demo purposes to show how to capture values since we are looking at 5 min intervals and only New Records they are only valid for the time we indexed the record.

Subreddit data saved to PoatgresSQL.

![alt text](https://user-images.githubusercontent.com/105808631/181680969-a60c94df-3dfc-4841-9b97-ade10c7beb95.png)

Using the YARP engine for ral time Covid news:






