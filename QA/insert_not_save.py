#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-07-14 09:40:18

from mongoengine import *

connect('test')
class User(Document):
    name = StringField()
    
    def sayhi(self):
        print('Hello, my name is %s' % self.name)
    def save(self):
        print('saving user %s...' % self.name)
        super(User, self).save()
    def __str__(self):
        return self.name

User.objects.delete()
John = User(name='John')
John.sayhi()
John.save()

Ross = User(name='Ross')
Ross.sayhi()
User.objects.insert(Ross)

for i in User.objects.all():
    print(i)
