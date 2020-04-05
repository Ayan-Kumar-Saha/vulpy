import csv
from datetime import datetime, timezone
from dateutil import parser

def write_to_csv(file, twitter_data):
    """Writes tweeter data to a csv file
    
    Arguments:
        file {string} -- Name of the csv file where data needs to be written
        twitter_data {dict} -- Dictionary that contains tweeter data
    """

    with open(file, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Username', 'Handle', 'Date', 'Time', 'Message', 'Replies', 'Retweets', 'Likes'])

        for handle in twitter_data:

            username = twitter_data[handle]['Username']
            post_date = twitter_data[handle]['Date']
            post_time = twitter_data[handle]['Time']
            message = twitter_data[handle]['Message']
            replies = twitter_data[handle]['Replies']
            retweets = twitter_data[handle]['Retweets']
            likes = twitter_data[handle]['Likes']

            csv_writer.writerow([username, handle, post_date, post_time, message, replies, retweets, likes])

        csvfile.close()


def parse_to_datetime(date_string):
    """Returns a datetime object by parsing an ISO format datetime string
    
    Arguments:
        date_string {string} -- String representing datetime in ISO format
    
    Returns:
        datetime -- datetime object
    """
    return parser.isoparse(date_string)
    
    
def utc_to_local(utc_time):
    """Converts and returns a utc datetime object to a local timezone datetime object
    
    Arguments:
        utc_time {datetime} -- utc datetime object
    
    Returns:
        datetime -- local timezone datetime object 
    """
    return utc_time.replace(tzinfo=timezone.utc).astimezone(tz=None)


def get_date(datetime_obj):
    """Returns date as a string from the datetime object
    
    Arguments:
        datetime_obj {datetime} -- datetime object
    
    Returns:
        string -- date as a formatted string
    """
    return datetime_obj.date().strftime('%d-%m-%Y')


def get_time(datetime_obj):
    """Returns time as a string from the datetime object
    
    Arguments:
        datetime_obj {datetime} -- datetime object

    Returns:
        string -- time as a formatted string
    """
    return datetime_obj.time().strftime('%I:%M %p')
