"""
A script to
- Read the Skype channel messages.
- Parse the messages with URLs and date of posting.
- Write ths parsed into into a CSV file.
"""
from skpy import Skype
import skype_config as sc
import skype_credentials as cred
import re

def read_skype_messages():
    # Read all messages from the Skype channel.
    sk = Skype(cred.skype_username, cred.skype_password)
    channel = sk.chats.chat(sc.channel_id)
    return channel.getMsgs()

def parse_skype_messages(msgs):
    # Parse to retrieve the links and date from skype messages.
    newsletter_data = [] # list of lists
    for msg in msgs:
        link_match = re.search(r'href=[\'"]?([^\'" >]+)', str(msg))
        if link_match:
            print ('\n Message is :\n{}'.format(msg))
            print('\n Posted link is : {}'.format(link_match.group(1)))
            date_match = re.search(r'20[0-9]+[0-9]+[\-]+[0-9]+[\-]+[0-9]+',str(msg))
            if date_match:
                print('\n Posted date is : {}'.format(date_match.group(0)))
                newsletter_data.append([date_match.group(0), link_match.group(1)])
    # Write the parsed skype links info into a csv.
    write_data_into_csv(newsletter_data)

def write_data_into_csv(records):
    # Write the parsed skype info into a CSV file.
    with open(sc.csv_filename,'a') as fp:
        for record in records:
            fp.write(",".join(str(value) for value in record) + "\n")

if __name__ == "__main__":
    messages = read_skype_messages()
    parse_skype_messages(messages)



