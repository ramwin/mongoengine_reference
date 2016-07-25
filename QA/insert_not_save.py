#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-07-14 09:40:18

from mongoengine import *

connect('test')
class User(Document):
    name = StringField()
    
    def sayhi(self):
        print('Hello, my name is %s' % self.name)
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        print('saving user %s...' % self.name)
        super(User, self).save()
    def __str__(self):
        return self.name

User.objects.delete()
John = User(name='John')
John.sayhi() # Hello, my name is John
John.save() # nothing

Ross = User(name='Ross')
Ross.sayhi() # Hello, my name is Ross
User.objects.insert(Ross) # there is no `saving user Ross...`

for i in User.objects.all():
    print(i)
# John
# Ross
