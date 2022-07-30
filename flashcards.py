# Spaced Repition Flashcards
# Create new cards and answer old ones at random
# Prioritize cards that have been answered incorrectly
import sqlite3
from datetime import date
from random import sample

db = sqlite3.connect('deck.db')
cursor = db.cursor()
topics = ['app sec']


def add_card(quest, ans, top, forgot, date):
    if not top in topics:
        topics.append(top)
    card = f'''INSERT INTO deck (question, answer, topic, forgotten, date) VALUES (\"{quest}\", \"{ans}\", \"{top}\", {forgot}, {date})'''
    cursor.execute(card)
    db.commit()
    print('Card added Successfully\n')


def start():
    print('\nHello, welcome to the Flashcards app. Which topic would you like to train?\n')
    for i in range(len(topics)):
        num = i + 1
        print(f'{num}. {topics[i]}')
    print('\nTo add a new card, press \'n\'')
    print('To exit, press \'e\'\n')
    
    ans = input('> ')
    if ans == 'n':
        q = input('Enter the question: ')
        a = input('Enter the answer: ')
        t = input('Enter the topic: ')
        f = 0
        today = date.today()
        add_card(q, a, t, f, today)

    elif ans == 'e':
        exit()

    else: flash(topics[int(ans)-1])
    start()


def flash(topic):
    query = f'''SELECT question, answer FROM deck WHERE topic = \"{topic}\"'''
    qna = cursor.execute(query).fetchall()
    i = 1
    for q, a in sample(qna, 10):
        input(f'{i}. {q} \n\n\n\nPress enter\n\n\n\n')
        input(f'{i}. {a} \n\n\n\nPress enter\n\n\n\n')
        i += 1


start()

