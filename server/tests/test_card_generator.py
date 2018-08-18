'''
    module for testing card generator

    [] parse csv and save in database
    [] get collection from database
    [] sort by wrong answers, importance, frequency
    [] return a list of documents
'''

import logging
from modules import card_generator
import pymongo
import unittest

logging.basicConfig(level=logging.DEBUG)

client = pymongo.MongoClient()
db = client.flashcards


class TestCardGenerator(unittest.TestCase):
    ''' test class for card generator'''

    def setUp(self):
        ''' function that gets run before each unit test '''
        print(' Setting up before next unit test... ')
        pass

    def tearDown(self):
        ''' function that gets run after each unit test '''
        print(' Cleaning up from last unit test... ')
        pass

    def test_always_works(self):
        ''' sample unit test '''
        logging.debug('\n\ninfo about test: assert True == True\n\n')
        self.assertTrue(True)

    def test_save_to_db(self):
        ''' unit test to check parsing csv and saving to database '''
        test_file_name = "test_word_meaning.csv"
        username = "test_user"
        card_generator.parse_csv_into_cards(test_file_name, username)
        test_collection_name = username + '_' + test_file_name[:-4]
        self.assertTrue(db[test_collection_name].count() != 0)

    def test_get_documents_from_db(self):
        ''' unit test to check sorting by parameters '''
        cardset_name = "test_user_test_word_meaning"
        cards_list = card_generator.create_cards(cardset_name)
        flag = True
        prev = 100
        for c in cards_list:
            if prev < c['wrong_count']:
                flag = False
                break
            else:
                prev = c['wrong_count']
        self.assertTrue(flag)


def main():
    return unittest.main()


if __name__ == '__main__':
    main()
