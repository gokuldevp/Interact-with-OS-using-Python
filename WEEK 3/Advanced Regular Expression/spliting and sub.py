import re


def split_wo_sep(line):
    """split without separators"""
    regex = r"[.?!]"
    return re.split(regex, line)


def split_w_sep(line):
    """split with separators"""
    regex = r"([.?!])"
    return re.split(regex, line)


def anonymize_email(line):
    """anonymous email address"""
    regex = r"[\w.%+-]+@[\w.-]+"
    return re.sub(regex, "[anonymous]", line)


def rearranging_name(name):
    """rearranging name using sub"""
    regex = r"^([\w \.-]*), ([\w \.-]*)$"
    return re.sub(regex, r"\2 \1", name)


line1 = "I also have a! taste for hot? chocolate in the afternoon."
line2 = "This is my email address gokul@gmail.com"
name1 = "Dev, gokul"
print(split_wo_sep(line1))
print(split_w_sep(line1))
print(anonymize_email(line2))
print(rearranging_name(name1))

