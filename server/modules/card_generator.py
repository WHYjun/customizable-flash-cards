'''
    card generator module
    [x] parse csv and save in database
    [x] get collection from database
    [x] sort by wrong_count
    [] sort by importance
    [] sort by frequency
    [] create a list of cards (random but weighted)
    [x] return a list of cards
'''

import logging
import os
import pandas as pd
import pymongo

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('logs/card_generator.log')
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

client = pymongo.MongoClient()
db = client.flashcards


def create_cards(cardset_name):
    card_list = list(db[cardset_name].find().sort('wrong_count', -1))
    cardset = []
    # TODO : Implement random card list creation
    while(len(cardset) < 50):
        cardset.append(card_list.pop())
    return cardset


def parse_csv_into_cards(filename, username):
    '''
        get csv file from user input and parse each row into card
        and save to database as filename_username
    '''
    folder_path = os.environ.get("FOLDER_PATH")
    file_path = folder_path + "/" + filename
    try:
        df = pd.read_csv(file_path)
    except Exception:
        logger.error("FileNotFoundError:'{}'".format(file_path))
        return None
    fieldnames = []
    for row in df:
        fieldnames.append(row)
    cards = []
    for index in range(df.shape[0]):
        card = {}
        card['front'] = df[fieldnames[0]][index]
        card['back'] = df[fieldnames[1]][index]
        card['wrong_count'] = 0
        cards.append(card)
    collection_name = username + '_' + filename[:-4]
    db[collection_name].insert_many(cards)
