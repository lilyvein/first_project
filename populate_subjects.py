import os
import random
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Subject


def populate(n=9):
    # print(n)
    for entry in range(n):

        subject_list = ['Ajalugu', 'Eesti keel', 'Keemia', 'Kirjandus',
                        'Klassitund', 'Muusika', 'Geograafia', 'Füüsika', 'Bioloogia']

        # print(f'{subject_list}')
        # New Entry to Subjects table
        Subject.objects.get_or_create(subject=random.choices(subject_list)[0])


populate(9)  # teeb 5 inimest
#  populate(20) # teeb 20
