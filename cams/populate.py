#first configuring settings for the startproject
#Setting default settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

#import django and set it up
import django
django.setup()

#Fake pop scripts

import random
from camsapp.models import AccessRecord,Webpage,Topic,User
from faker import Faker

#create fakegen object
fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']


def add_topic():
    #get_or_create will return a tuple and we will take the first object in that tuple
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top=add_topic()

        #Create the fake data for that entry
        fake_url= fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email=fakegen.email()

        #new entry
        user=User.objects.get_or_create(first_name=fake_first_name,
        last_name=fake_last_name, email=fake_email)[0]
        #Create the new webpage entry
        webpg =Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake webpage record for that Webpage
        acc_rec= AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ =='__main__':
    print("populating scripts!")
    populate(20)
    print("populating complete")
