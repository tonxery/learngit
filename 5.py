#!/usr/bin/env python
#-*- coding:utf-8 -*-
def fengexian():
    print('*'*25)
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4212.')
print(mo.group(1))
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print mo1.group()
mo2 = heroRegex.search('Tina Fey and Batman.')
print '*'* 25
print mo2.group()
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel Batbat')
print mo.group()
print mo.group(1)
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print '#'*25
print mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
print mo2.group()
fengexian()
phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo3 = phoneNumRegex.search('My mumber is 415-555-7890')
print mo3.group()
mo4 = phoneNumRegex.search('You number is 567-8990')
print mo4.group()
fengexian()
batRegex = re.compile(r'Bat(wo)*man')
mo5 = batRegex.search('The adventures of Batman')
print mo5.group()
mo6 = batRegex.search('The adventures of Batwoman')
print mo6.group()
mo7 = batRegex.search('The adventures of Batwowowowoman')
print mo7.group()
batRegex = re.compile(r'Bat(wo)+man')
mo8 = batRegex.search('The Adventures of Batwoman')
fengexian()
print mo8.group()
mo9 = batRegex.search('The adventures of Batwowowoman')
print mo9.group()
mo10 = batRegex.search('Batman')
print mo10 == None
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print mo1.group()
mo2 = haRegex.search('Ha')
print mo2 == None
fengexian()
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print mo1.group()
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print mo2.group()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-9999 work:212-555-8888')
print mo
fengexian()
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 work:212-555-8888')
print mo1
xmasRegex = re.compile(r'\d+\s\w+')
mo2 = xmasRegex.findall('12 drummers,11 pipers,10 lords,9 ladies,8 maids,7 swans,6 geese,5 rings,4 birds,3 hens,2 doves,1 partridge')
print mo2
vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo3 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print mo3
fengexian()
beginsWithHello = re.compile(r'^Hello')
mo4 = beginsWithHello.search('Hello world!')
print(mo4.group())
mo5 = beginsWithHello.search('hi said hello.')
print(mo5 == None)
endsWithNumber = re.compile(r'\d$')
mo6 = endsWithNumber.search('Your number is 42')
print(mo6.group())
mo7 =  endsWithNumber.search('your number is forty two.')
print(mo7 == None)
wholeStringIsNum = re.compile(r'^\d+$')
mo8 = wholeStringIsNum.search('12343843')
print(mo8.group())
mo9 = wholeStringIsNum.search('12343xy888')
print(mo9==None)
atRegex = re.compile(r'.at')
mo9 = atRegex.findall('The cat in the hat sat on the flat mat.')
print mo9
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo10 = nameRegex.search('First Name:A1 Last Name: Sweigart')
print mo10.group(1)
print mo10.group(2)

nongreedyHaRegex = re.compile(r'<.*?>')
mo = nongreedyHaRegex.search('<To serve man> for dinner.>')
print mo.group()

greedyHaRegex = re.compile(r'<.*>')
mo11 = greedyHaRegex.search('<To serve man> for dinner.>')
print mo11.group()
fengexian()
noNewlineRegex = re.compile(r'.*')
mo12 =noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUpload the law.')
print(mo12.group())
fengexian()
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
\d{3}
(\s|-|\.)
\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?

                         )''',re.VERBOSE)

mo13 = phoneRegex.search('My phone number is 010-555-8888')
print mo13.group()
mo14 = phoneRegex.search('you phone number is 555-6666')
print mo14.group()


