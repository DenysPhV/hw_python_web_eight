import argparse
from _datetime import datetime
import json
from models import Author, Quotes

parser = argparse.ArgumentParser(description='load or find')
parser.add_argument('-a', '--action')


def load_json():
    with open('json/authors.json', 'r', encoding='utf-8') as fh:
        result = json.load(fh)

        for i in result:
            new_author = Author()
            new_author.description = i['description']
            new_author.born_date = datetime.strptime(i['born_date'], '%B %d, %Y').date()
            new_author.born_location = i['born_location']
            new_author.fullname = i['fullname']
            new_author.save()

    with open('json/qoutes.json', 'r', encoding='utf-8') as fh:
        rez = json.load(fh)
        for i in rez:
            authors = Author.objects(fullname=i['author'])
            if len(authors) > 0:
                cur_author = [0]
            new_quote = Quotes(author=cur_author)
            new_quote.quote = i['quote']
            new_quote.tags = i['tags']
            new_quote.save()


def find_in_db():
    while True:
        command = input('insert command and volume:')

        if command[:4] == 'exit':
            break

        else:
            arg = command.split(':')
            f_name = arg[0]

            if f_name == 'name':
                authors = Author.objects(fullname=arg[1])

                for author in authors:
                    print(author.to_mongo().to_dict())

            if f_name == 'tag':
                quotes = Quotes.objects(tags=arg[1])

                for quote in quotes:
                    print(quote.to_mongo().to_dict())

            if f_name == 'tag':
                quotes = Quotes.objects(tags__in=arg[1].split(' '))

                for quote in quotes:
                    print(quote.to_mongo().to_dict())


if __name__ == '__main__':
    if 'load' == vars(parser.parse_args()).get('action'):
        load_json()
    find_in_db()
