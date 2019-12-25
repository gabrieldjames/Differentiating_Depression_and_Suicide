import pandas as pd
import numpy as np
import praw
from praw.models import MoreComments
import datetime



def pull_Reddit_Posts(subreddit, num_posts):

	reddit = praw.Reddit(client_id='KvRsJ7d8P0y7sQ', client_secret='lp3sUKus_afFOSKcYMtVWDOElso', user_agent='Text1_Scraper')

	subreddit = reddit.subreddit(subreddit)

	posts = []
	comments = []
	comments_fo = []


	#get posts
	for post in subreddit.hot(limit=num_posts):
	    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, datetime.datetime.fromtimestamp(post.created)])

	posts = pd.DataFrame(posts,columns=['title', 'score', 'p_id', 'subreddit', 'url', 'num_comments', 'body', 'p_timestamp'])

	#get all comments, identify first-order comments
	for post_id in posts['p_id']:
		submission = reddit.submission(id=post_id)
		for top_level_comment in submission.comments.list(): #get all comments
			if isinstance(top_level_comment, MoreComments):
				continue
			comments.append([post_id, top_level_comment.id, top_level_comment.body, datetime.datetime.fromtimestamp(top_level_comment.created)])

		for top_level_comment in submission.comments: #get all first-order comments
			comments_fo.append([top_level_comment.id, 'Y'])



	comments_fo = pd.DataFrame(comments_fo, columns=['c_id', 'Post_Reply'])
	comments = pd.DataFrame(comments, columns=['p_id', 'c_id', 'comment', 'c_timestamp'])


	df = pd.merge(pd.merge(posts, comments, how='left', on='p_id'), comments_fo, how='left', on='c_id')
	df['Time_to_Comment'] = df['c_timestamp'] - df['p_timestamp']
	df['Post_Reply'] = df['Post_Reply'].fillna('N')

	return df


pull_Reddit_Posts('depression', 10000).to_csv('depression_posts.csv', index=False)
pull_Reddit_Posts('suicidewatch', 10000).to_csv('suicidewatch_posts.csv', index=False)

