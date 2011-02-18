from __future__ import absolute_import
from __future__ import with_statement

import getpass

def ask(question, default=None, blank=False):
    prompt = question + (default and ' [%s]'%default or '')
    prompt += question.endswith('?') and ' ' or ': '
    while True:
        answer = raw_input(prompt)
        if answer:
            return answer
        elif default is not None:
            return default
        elif blank:
            return None

def password(question='Enter your password'):
    question += question.endswith(':') and ' ' or ': '
    while True:
        answer = getpass.getpass(question)
        if answer:
            return answer
        if default is not None:
            return default

def yes(question, default=False):
    yes_choices = ('y', 'yes', '1', 'on', 'true', 't')
    no_choices = ('n', 'no', '0', 'off', 'false', 'f')
    answer = ask(question, default and yes_choices[0] or no_choices[0])
    if answer.lower() in yes_choices:
        return True
    elif answer.lower() in no_choices:
        return False
    else:
        return default

