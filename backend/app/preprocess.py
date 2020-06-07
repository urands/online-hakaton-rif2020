import re

def remove_spaces(text):
    return " ".join(text.split())
    # return re.sub(' +', ' ', text)

def pretty_comma(text):
    return  re.sub(r'\s*,\s*', ', ', text)

def pretty_slash(text):
    return  re.sub(r'\s*[\\|/]\s*', '/', text)

def pretty_dot(text):
    return  text.replace('.','. ').strip(' *"\',.')