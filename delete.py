import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
import django
django.setup()
from catalog.models import Genre

def main():
    Genre.objects.all().delete()


if __name__ == '__main__':

    main()