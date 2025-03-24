import re


def extract_pid(log_line):
    pattern = r"\[(\d+)\]"
    result = re.search(pattern, log_line)

    if result is None:
        return None
    return result[1]


log1 = "my computer bad_process[12945]: ERROR while upgrade"
log2 = "my computer bad_process12945]: ERROR while upgrade"
log3 = "my computer bad_process[apple]: ERROR while upgrade"
log4 = "my computer bad_process[]: ERROR while upgrade"

print(extract_pid(log1))
print(extract_pid(log2))
print(extract_pid(log3))
print(extract_pid(log4))


# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis,
# after the process id.
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)
