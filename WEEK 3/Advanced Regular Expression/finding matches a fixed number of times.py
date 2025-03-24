import re


def find_matches(string):
    result = re.findall(r"[a-zA-Z]{5}", string)
    return result


print(find_matches("gokul dev is a smart boy, right people"))


# to ger full words
def find_matches(string):
    result = re.findall(r"\b[a-zA-Z]{5}\b", string)
    return result


print(find_matches("gokul dev is a smart boy, right people"))


# to get range of words till a limit
def find_matches(string):
    result = re.findall(r"[a-zA-Z]{5,10}", string)
    return result


print(find_matches("gokul dev is a smart boy, right people of the universespectrum"))


# to get range of words till infinity
def find_matches(string):
    result = re.findall(r"\b[a-zA-Z]{5,}\b", string)
    return result


print(find_matches("gokul dev is a smart boy, right people of the universespectrum"))


# The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete
# this function.
def long_words(text):
    pattern = r"\b\w{7,}\b"
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon."))  # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night."))  # []
