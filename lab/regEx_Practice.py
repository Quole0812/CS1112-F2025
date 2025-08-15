# CS 1112
# Learning Python (Python version: 3)
# Module 6: regEx Practice ACTIVITY

##### NOTE ON REGEX FUNCTIONS #####
'''
1. findall() - returns a list containing all matches
2. finditer() - returns the iterator of where the matches occur
2. search() - returns a match object if there is a match (if >1 match, only *FIRST* match is returned)
3. split() - returns a list where string is split at each match
4. sub() - replaces matches with text of choice
*if you would like more information on match objects, there are resources online with in-depth explanations
'''

import re
# QUESTION 1
'''
Match all words that begin with the letter "a" and end with the letter "e".
The words can contain any number of characters between the first and last letters.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
one = "apple"
q1 = re.findall(r" ", one)    # can also use the search function
print(q1)


# QUESTION 2
'''
Match all phone numbers in the format (123)456-7890. The area code and exchange can
be any three-digit number, and the final four digits can be any four-digit number.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
two = "(888)888-8888"
q2 = re.findall(r" ", two)   # issue: if another number is added in the number, it's still a match
print(q2)


# QUESTION 3
'''
Match all dates in the format MM/DD/YYYY, where MM is a two-digit month number, DD
is a two-digit day number, and YYYY is a four-digit year number.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
three = "08/30/2023"
q3 = re.findall(r" ", three)
print(q3)


# QUESTION 4
'''
Match all email addresses in the format username@domain.com. The username can contain any combination of letter,
numbers, periods, underscores, and hyphens. The domain name can contain any combination of letters and periods.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
four = "basit@virginia.edu"
q4 = re.findall(r" ", four)
print(q4)


# QUESTION 5
'''
Match all URLs that begin with "http://" or "https://". The URL can contain any
combination of letters, numbers, periods, underscores, and hyphens.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
five = "https://www.virginia.edu/"
q5 = re.search(r" ", five)
print(q5)

## *** Note about Question 5 ***
## Once you write the regular expression correctly the output will look different from the rest (due to the search() function)
## The output may look something like this:   <re.Match object; span=(0, 24), match='https://www.virginia.edu'>
## If you get an output that looks like this, then you got it right!
## ************


# QUESTION 6
'''
Match all credit card numbers in the format XXXX-XXXX-XXXX-XXXX, where X is a digit
from 0 to 9.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
six = "1234-1234-1234-1234"
q6 = re.findall(r" ", six)
print(q6)


# QUESTION 7
'''
Match all words that are exactly six letters long and begin with a vowel. The words
can contain any combination of letters between the first and last letters.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
seven = "aliens"
q7 = re.findall(r" ", seven)
print(q7)


# QUESTION 8
'''
Match all US zip codes in the format XXXXX or XXXXX-XXX, where X is a digit from 0 to 9.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
eight = "12321-331"
q8 = re.findall(r" ", eight)
print(q8)


# QUESTION 9
'''
Match all words that contain the letter "q" but do not end with the letter "u".
The words can contain any combination of letters.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
nine = "queue"
q9 = re.findall(r" ", nine)
print(q9)


# QUESTION 10
'''
Match all hashtags in a social media posts, which start with the pound sign (#)
and can contain any combination of letters and numbers.
'''
#### ADD your Regular Expression to the code below (in between the quotation marks)
ten = "#socialmedia123"
q10 = re.findall(r" ", ten)
print(q10)
