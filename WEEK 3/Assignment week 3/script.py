"""The aim of this script is to use regex to find all instances of the old domain ("abc.edu") in the user_emails.csv
file and then replace them with the new domain ("xyz.edu"). """
# !/usr/bin/env python3

# Import libraries
import csv
import re


def contains_domain(address, domain):
    """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
    domain_pattern = r'[\w\.-]+@' + domain + '$'
    if re.match(domain_pattern, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in
    the received address."""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main():
    """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    csv_file_location = '/home/student-01-95f65dba45a1/data/user_emails.csv'
    report_file = '/home/student-01-95f65dba45a1/data' + '/updated_user_emails.csv'
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]

        for email_address in user_email_list:

            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replace_email = replace_domain(email_address, old_domain, new_domain)
                new_domain_email_list.append(replace_email)

        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)

        for user in user_data_list[1:]:

            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):

                if user[email_index] == ' ' + old_domain:
                    user[email_index] = ' ' + new_domain

    f.close()

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()
