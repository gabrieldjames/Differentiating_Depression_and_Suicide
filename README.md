# Differentiating_Depression_and_Suicide
A text analytics project centered on understanding the r/Depression and r/SuicideWatch subreddits

Please see the PowerPoint deck or pdf for a summary of this project.

#### Data Collection
proj_scraper.py is the script I wrote to pull Reddit comments using PRAW.

depression_posts_scraped.csv, depression_comments.csv, suicidewatch_posts_scraped.csv, and suicidewatch_comments.csv were created from proj_scraper.py

#### Preprocessing
Frequencies_and_Sentiments.ipynb preprocesses the posts and comments and produces depression_threads.csv and suicide_watch.csv

#### Analysis
EDA.ipynb produces several useful density and MDS plots.
Topic_Modeling.ipynb is an attempt to assign topics to the r/Depression and r/SuicideWatch posts.
Classification.ipynb runs several predictive models to classify threads, including sentiment data and metadata, as r/Depression or r/SuicideWatch threads.
