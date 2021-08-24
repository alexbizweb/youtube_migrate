from selenium import webdriver
import csv
import time

file_csv = 'subscriptions.csv'


def csv_count_row():
    with open(file_csv, newline='', encoding="utf-8") as f:
        rd = csv.DictReader(f)
        count = len(list(rd))
        return count


print(f"[INFO] You have {csv_count_row()} subscriptions")

"""Read CSV file and get url for subscription"""
with open(file_csv, newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        channel_url = row['Channel URL']
        channel_name = row['Channel title']

        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data/')
        options.add_argument(r'--profile-directory=Profile 1')
        driver = webdriver.Chrome(options=options)

        """Open URL YouTube ID channel with Selenium"""
        url = channel_url
        driver.get(url)
        """Automatic click the button SUBSCRIBE"""
        button = driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper'
                                              '-button/yt-formatted-string')
        button.click()
        """Waiting 3 sec to continue"""
        time.sleep(3)
        driver.quit()
        print(f"{channel_name} added to your YouTube subscription list")
        """Waiting 5 minutes for new subscription"""
        time.sleep(60)
        print("[INFO] Waiting 1 minutes...")
