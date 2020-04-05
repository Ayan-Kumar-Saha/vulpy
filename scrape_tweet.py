import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import *

base_URL = 'https://twitter.com/search/?q='

hashtag = input('Enter hashtags(give space between two hashtag): ')

browser = webdriver.Firefox(executable_path = '/home/suvo/Desktop/geckodriver')
wait = WebDriverWait(browser, 20)

browser.get(base_URL + hashtag)
browser.maximize_window()

time.sleep(3)

wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
timeline = browser.find_element_by_tag_name('body')

twitter_data = dict()

tweet_count = 0

for i in range(10):

    tweets = browser.find_elements_by_css_selector('div[data-testid="tweet"]')

    for tweet in tweets:

        try: 
            reply = tweet.find_element_by_css_selector('div[data-testid="reply"]')
            retweets = tweet.find_element_by_css_selector('div[data-testid="retweet"]')
            likes = tweet.find_element_by_css_selector('div[data-testid="like"]')
            posted = tweet.find_element_by_css_selector('time').get_attribute('datetime')

            utc_posted_datetime = parse_to_datetime(posted)
            local_posted_datetime = utc_to_local(utc_posted_datetime)

            post_date = get_date(local_posted_datetime)

            post_time = get_time(local_posted_datetime)

            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-901oao.r-jwli3a.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0')))
            
            message = tweet.find_element_by_css_selector('.css-901oao.r-jwli3a.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0')

            account_data = tweet.text.split('\n')
            username = account_data[0]
            handle = account_data[1]
           
            if handle not in twitter_data:
                twitter_data[handle] = {
                    'Username': username,
                    'Date': post_date,
                    'Time': post_time,
                    'Message': message.text,
                    'Replies': reply.text,
                    'Retweets': retweets.text,
                    'Likes': likes.text
                }
                tweet_count += 1   
                print('Tweet #' + str(tweet_count))

        except Exception as e:
            pass

    timeline.send_keys(Keys.PAGE_DOWN)
    print('page down count: ' + str(i+1))

    time.sleep(0.2)

write_to_csv('tweets.csv', twitter_data)

print('Total tweets: ' + str(tweet_count))
browser.quit()
