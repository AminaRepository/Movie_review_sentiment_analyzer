#!/usr/bin/env python
# coding: utf-8

# In[56]:


import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

def get_rotten_tomatoes_comments(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    comments = []
    for comment in soup.find_all('div', class_='review-row'):
        text = comment.find('p', class_='review-text')
        if text:
            comments.append(text.get_text(strip=True))

    #for i, comment in enumerate(comments, start=1):
    #    sentiment = analyzer.polarity_scores(comment)['compound']
    #    print(f"Comment {i}: {comment} - Sentiment: {sentiment}")

    return comments

def adjust_sentiment_score(compound_score):
    adjusted_score = (compound_score + 1) / 2
    return adjusted_score

def analyze_sentiment(comments):
    analyzer = SentimentIntensityAnalyzer()
    total_sentiment = 0.0
    
    if not comments:
        return total_sentiment
    
    for comment in comments:
        #sentiment = analyzer.polarity_scores(comment)['compound']
        sentiment = adjust_sentiment_score(analyzer.polarity_scores(comment)['compound'])
        total_sentiment = total_sentiment + sentiment
    
    return total_sentiment / len(comments)

def get_audience_score(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    audience_score = soup.find_all('div', class_='percentage')
    score = audience_score.find('p', class_='audience-score')
    
    return score

def average_sentiment_from_link(link):
    comments = get_rotten_tomatoes_comments(link)
    avg_sentiment = analyze_sentiment(comments)
    return avg_sentiment

def sentiment_difference(average, movie_rating):
    difference = abs(average - movie_rating)
    return difference


# In[60]:


# general test
differences = []

# titanic movie
link = 'https://www.rottentomatoes.com/m/titanic/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.88))
print(f'Average sentiment for comments on Titanic: {average}')

# matrix movie
link = 'https://www.rottentomatoes.com/m/matrix/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.83))
print(f'Average sentiment for comments on Matrix: {average}')

# lotr movie
link = 'https://www.rottentomatoes.com/m/the_lord_of_the_rings_the_return_of_the_king/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.94))
print(f'Average sentiment for comments on Lord of the rings: {average}')

# barbie movie
link = 'https://www.rottentomatoes.com/m/barbie/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.88))
print(f'Average sentiment for comments on Barbie: {average}')

# home alone movie
link = 'https://www.rottentomatoes.com/m/home_alone/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.66))
print(f'Average sentiment for comments on Home alone: {average}')

# godfather movie
link = 'https://www.rottentomatoes.com/m/the_godfather/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.97))
print(f'Average sentiment for comments on Godfather: {average}')

# morbious movie
link = 'https://www.rottentomatoes.com/m/morbius/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.15))
print(f'Average sentiment for comments on Morbious: {average}')

# mario movie
link = 'https://www.rottentomatoes.com/m/the_super_mario_bros_movie/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.59))
print(f'Average sentiment for comments on Mario: {average}')

# top gun movie
link = 'https://www.rottentomatoes.com/m/top_gun/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.57))
print(f'Average sentiment for comments on Top gun: {average}')

# hocus pocus movie
link = 'https://www.rottentomatoes.com/m/hocus_pocus/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.40))
print(f'Average sentiment for comments on Hocus Pocus: {average}')

# space jam movie
link = 'https://www.rottentomatoes.com/m/space_jam/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.43))
print(f'Average sentiment for comments on Space Jam: {average}')

# potc movie
link = 'https://www.rottentomatoes.com/m/pirates_of_the_caribbean_the_curse_of_the_black_pearl/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.80))
print(f'Average sentiment for comments on Pirates of the Caribbean: {average}')

# nimona movie
link = 'https://www.rottentomatoes.com/m/nimona/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.95))
print(f'Average sentiment for comments on Nimona: {average}')

# oppenheimer movie
link = 'https://www.rottentomatoes.com/m/oppenheimer_2023/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.93))
print(f'Average sentiment for comments on Oppenheimer: {average}')

# scott pilgrim movie
link = 'https://www.rottentomatoes.com/m/scott_pilgrims_vs_the_world/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.82))
print(f'Average sentiment for comments on Scott Pilgrim VS the world: {average}')

# mean girls movie
link = 'https://www.rottentomatoes.com/m/mean_girls/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.84))
print(f'Average sentiment for comments on Mean girls: {average}')

# spirited away movie
link = 'https://www.rottentomatoes.com/m/spirited_away/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.96))
print(f'Average sentiment for comments on Spirited away: {average}')

# love simon movie
link = 'https://www.rottentomatoes.com/m/love_simon/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.92))
print(f'Average sentiment for comments on Love Simon: {average}')

# maleficent movie
link = 'https://www.rottentomatoes.com/m/maleficent_2014/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.54))
print(f'Average sentiment for comments on Maleficent: {average}')

# mamma mia movie
link = 'https://www.rottentomatoes.com/m/mamma_mia/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.55))
print(f'Average sentiment for comments on Mamma Mia: {average}')

# love actually movie
link = 'https://www.rottentomatoes.com/m/love_actually/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.64))
print(f'Average sentiment for comments on Love actually: {average}')

# the wolf of wallstreet movie
link = 'https://www.rottentomatoes.com/m/the_wolf_of_wall_street_2013/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.83))
print(f'Average sentiment for comments on The wolf of wallstreet: {average}')

# suicide squad movie
link = 'https://www.rottentomatoes.com/m/suicide_squad_2016/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.26))
print(f'Average sentiment for comments on Suicide squad: {average}')

# mr&mrs smith movie
link = 'https://www.rottentomatoes.com/m/mr_and_mrs_smith/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.60))
print(f'Average sentiment for comments on Mr&Mrs Smith: {average}')

# anna karenina movie
link = 'https://www.rottentomatoes.com/m/anna_karenina_2012/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.63))
print(f'Average sentiment for comments on Anna Karenina: {average}')

# pride and prejudice movie
link = 'https://www.rottentomatoes.com/m/1153077-1153077-pride_and_prejudice/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.87))
print(f'Average sentiment for comments on Pride and Prejudice: {average}')

# persuasion movie
link = 'https://www.rottentomatoes.com/m/persuasion/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.31))
print(f'Average sentiment for comments on Persuasion: {average}')

# oceans 11 movie
link = 'https://www.rottentomatoes.com/m/oceans_eleven/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.83))
print(f'Average sentiment for comments on Oceans eleven: {average}')

# tangled movie
link = 'https://www.rottentomatoes.com/m/tangled/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.89))
print(f'Average sentiment for comments on Tangled: {average}')

# the last wish movie
link = 'https://www.rottentomatoes.com/m/puss_in_boots_the_last_wish/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.95))
print(f'Average sentiment for comments on The last wish: {average}')

# national treasure movie
link = 'https://www.rottentomatoes.com/m/national_treasure/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.46))
print(f'Average sentiment for comments on National treasure: {average}')

# saw movie
link = 'https://www.rottentomatoes.com/m/saw/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.5))
print(f'Average sentiment for comments on Saw: {average}')

# hook movie
link = 'https://www.rottentomatoes.com/m/hook/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.29))
print(f'Average sentiment for comments on Hook: {average}')

# armageddon movie
link = 'https://www.rottentomatoes.com/m/armageddon/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.43))
print(f'Average sentiment for comments on Armageddon: {average}')

# fnaf movie
link = 'https://www.rottentomatoes.com/m/five_nights_at_freddys/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.32))
print(f'Average sentiment for comments on Fife nights at Freddies: {average}')

# meg2 movie
link = 'https://www.rottentomatoes.com/m/meg_2_the_trench/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.27))
print(f'Average sentiment for comments on Meg 2: {average}')

# new years eve movie
link = 'https://www.rottentomatoes.com/m/new_years_eve_2011/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.07))
print(f'Average sentiment for comments on New years eve: {average}')

# expendables movie
link = 'https://www.rottentomatoes.com/m/expend4bles/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.14))
print(f'Average sentiment for comments on Expendables: {average}')

# batman v superman movie
link = 'https://www.rottentomatoes.com/m/batman_v_superman_dawn_of_justice/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.29))
print(f'Average sentiment for comments on Batman v Superman: {average}')

# uncharted movie
link = 'https://www.rottentomatoes.com/m/uncharted_2022/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.4))
print(f'Average sentiment for comments on Uncharted: {average}')

# dominion movie
link = 'https://www.rottentomatoes.com/m/jurassic_world_dominion/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.29))
print(f'Average sentiment for comments on Dominion: {average}')


# In[61]:


# average movie differences

average_difference = 0.0

for difference in differences:
    average_difference = average_difference + difference
    
print("Average difference: ", average_difference/len(differences))
print("Biggest difference: ", max(differences))
print("Smallest difference: ", min(differences))


# In[62]:


# low rated movie test
differences = []

# morbious movie
link = 'https://www.rottentomatoes.com/m/morbius/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.15))
print(f'Average sentiment for comments on Morbious: {average}')

# hocus pocus movie
link = 'https://www.rottentomatoes.com/m/hocus_pocus/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.40))
print(f'Average sentiment for comments on Hocus Pocus: {average}')

# space jam movie
link = 'https://www.rottentomatoes.com/m/space_jam/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.43))
print(f'Average sentiment for comments on Space Jam: {average}')

# suicide squad movie
link = 'https://www.rottentomatoes.com/m/suicide_squad_2016/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.26))
print(f'Average sentiment for comments on Suicide squad: {average}')

# persuasion movie
link = 'https://www.rottentomatoes.com/m/persuasion/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.31))
print(f'Average sentiment for comments on Persuasion: {average}')

# national treasure movie
link = 'https://www.rottentomatoes.com/m/national_treasure/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.46))
print(f'Average sentiment for comments on National treasure: {average}')

# saw movie
link = 'https://www.rottentomatoes.com/m/saw/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.5))
print(f'Average sentiment for comments on Saw: {average}')

# hook movie
link = 'https://www.rottentomatoes.com/m/hook/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.29))
print(f'Average sentiment for comments on Hook: {average}')

# armageddon movie
link = 'https://www.rottentomatoes.com/m/armageddon/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.43))
print(f'Average sentiment for comments on Armageddon: {average}')

# fnaf movie
link = 'https://www.rottentomatoes.com/m/five_nights_at_freddys/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.32))
print(f'Average sentiment for comments on Fife nights at Freddies: {average}')

# meg2 movie
link = 'https://www.rottentomatoes.com/m/meg_2_the_trench/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.27))
print(f'Average sentiment for comments on Meg 2: {average}')

# new years eve movie
link = 'https://www.rottentomatoes.com/m/new_years_eve_2011/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.07))
print(f'Average sentiment for comments on New years eve: {average}')

# expendables movie
link = 'https://www.rottentomatoes.com/m/expend4bles/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.14))
print(f'Average sentiment for comments on Expendables: {average}')

# batman v superman movie
link = 'https://www.rottentomatoes.com/m/batman_v_superman_dawn_of_justice/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.29))
print(f'Average sentiment for comments on Batman v Superman: {average}')

# uncharted movie
link = 'https://www.rottentomatoes.com/m/uncharted_2022/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.4))
print(f'Average sentiment for comments on Uncharted: {average}')

# dominion movie
link = 'https://www.rottentomatoes.com/m/jurassic_world_dominion/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.29))
print(f'Average sentiment for comments on Dominion: {average}')


# In[63]:


# low rated movie differences

average_difference = 0.0

for difference in differences:
    average_difference = average_difference + difference
    
print("Average difference: ", average_difference/len(differences))
print("Biggest difference: ", max(differences))
print("Smallest difference: ", min(differences))


# In[64]:


# high rated movie test
differences = []

# titanic movie
link = 'https://www.rottentomatoes.com/m/titanic/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.88))
print(f'Average sentiment for comments on Titanic: {average}')

# matrix movie
link = 'https://www.rottentomatoes.com/m/matrix/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.83))
print(f'Average sentiment for comments on Matrix: {average}')

# lotr movie
link = 'https://www.rottentomatoes.com/m/the_lord_of_the_rings_the_return_of_the_king/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.94))
print(f'Average sentiment for comments on Lord of the rings: {average}')

# barbie movie
link = 'https://www.rottentomatoes.com/m/barbie/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.88))
print(f'Average sentiment for comments on Barbie: {average}')

# home alone movie
link = 'https://www.rottentomatoes.com/m/home_alone/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.66))
print(f'Average sentiment for comments on Home alone: {average}')

# godfather movie
link = 'https://www.rottentomatoes.com/m/the_godfather/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.97))
print(f'Average sentiment for comments on Godfather: {average}')

# potc movie
link = 'https://www.rottentomatoes.com/m/pirates_of_the_caribbean_the_curse_of_the_black_pearl/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.80))
print(f'Average sentiment for comments on Pirates of the Caribbean: {average}')

# nimona movie
link = 'https://www.rottentomatoes.com/m/nimona/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.95))
print(f'Average sentiment for comments on Nimona: {average}')

# oppenheimer movie
link = 'https://www.rottentomatoes.com/m/oppenheimer_2023/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.93))
print(f'Average sentiment for comments on Oppenheimer: {average}')

# scott pilgrim movie
link = 'https://www.rottentomatoes.com/m/scott_pilgrims_vs_the_world/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.82))
print(f'Average sentiment for comments on Scott Pilgrim VS the world: {average}')

# mean girls movie
link = 'https://www.rottentomatoes.com/m/mean_girls/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.84))
print(f'Average sentiment for comments on Mean girls: {average}')

# spirited away movie
link = 'https://www.rottentomatoes.com/m/spirited_away/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.96))
print(f'Average sentiment for comments on Spirited away: {average}')

# love simon movie
link = 'https://www.rottentomatoes.com/m/love_simon/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.92))
print(f'Average sentiment for comments on Love Simon: {average}')

# maleficent movie
link = 'https://www.rottentomatoes.com/m/maleficent_2014/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.54))
print(f'Average sentiment for comments on Maleficent: {average}')

# mamma mia movie
link = 'https://www.rottentomatoes.com/m/mamma_mia/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.55))
print(f'Average sentiment for comments on Mamma Mia: {average}')

# love actually movie
link = 'https://www.rottentomatoes.com/m/love_actually/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.64))
print(f'Average sentiment for comments on Love actually: {average}')

# the wolf of wallstreet movie
link = 'https://www.rottentomatoes.com/m/the_wolf_of_wall_street_2013/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.83))
print(f'Average sentiment for comments on The wolf of wallstreet: {average}')

# mr&mrs smith movie
link = 'https://www.rottentomatoes.com/m/mr_and_mrs_smith/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.60))
print(f'Average sentiment for comments on Mr&Mrs Smith: {average}')

# anna karenina movie
link = 'https://www.rottentomatoes.com/m/anna_karenina_2012/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.63))
print(f'Average sentiment for comments on Anna Karenina: {average}')

# pride and prejudice movie
link = 'https://www.rottentomatoes.com/m/1153077-1153077-pride_and_prejudice/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.87))
print(f'Average sentiment for comments on Pride and Prejudice: {average}')

# oceans 11 movie
link = 'https://www.rottentomatoes.com/m/oceans_eleven/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.83))
print(f'Average sentiment for comments on Oceans eleven: {average}')

# tangled movie
link = 'https://www.rottentomatoes.com/m/tangled/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.89))
print(f'Average sentiment for comments on Tangled: {average}')

# the last wish movie
link = 'https://www.rottentomatoes.com/m/puss_in_boots_the_last_wish/reviews?intcmp=rt-what-to-know_read-critics-reviews'
average = average_sentiment_from_link(link)
differences.append(sentiment_difference(average, 0.95))
print(f'Average sentiment for comments on The last wish: {average}')


# In[65]:


# high rated movie differences

average_difference = 0.0

for difference in differences:
    average_difference = average_difference + difference
    
print("Average difference: ", average_difference/len(differences))
print("Biggest difference: ", max(differences))
print("Smallest difference: ", min(differences))


# In[ ]:




