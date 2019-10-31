# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','library.settings')
#
# import django
# django.setup()
#
# import random
# from ../catalog.models import Book, Author,Genre, Language
# from faker import Faker
#
# fakegen = Faker('ru-RU')
#
# topics = ['Search', 'Marketplace', 'News']
#
# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t
#
# def populate(N=5):
#
#     for entry in range(N):
#         top = add_topic()
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()
#
#         ganre = Genre.objects
#
#
# if __name__== '__main__':
#     print('Populate database!')
#     populate(100)
#     print('Population complete!')