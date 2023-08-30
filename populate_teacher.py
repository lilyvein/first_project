import os
import random
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Teacher

fakegen = Faker()


def populate(n=10):
    # print(n)
    for entry in range(n):
        fake_name = fakegen.name()
        subject_list = ['history', 'music', 'biology', 'geology']

        print(f'{fake_name}, {subject_list}')
        # New Entry to Student table
        Teacher.objects.get_or_create(name=fake_name, subject=random.choices(subject_list)[0])


populate()  # teeb 5 inimest
# populate(20) # teeb 20