from secrets import LOCAL_MYSQL_HOST, LOCAL_MYSQL_PASSWORD

import requests
from datetime import datetime, timedelta
import mysql.connector
import time
import os

def get_last_fetched_date():
    if os.path.exists('last_fetched_date.txt'):
        with open('last_fetched_date.txt', 'r') as file:
            last_fetched_date_str = file.readline()
            return datetime.strptime(last_fetched_date_str, '%Y-%m-%d').date()
    else:
        return datetime.strptime('2023-01-24', '%Y-%m-%d').date()

def update_last_fetched_date(date):
    with open('last_fetched_date.txt', 'w') as file:
        file.write(date.strftime('%Y-%m-%d'))

def generate_dates(start_date):
    end_date = datetime.now().date()
    delta = timedelta(days=1)
    
    current_date = start_date
    dates = []
    while current_date <= end_date:
        dates.append(current_date)
        current_date += delta
    
    return dates

def fetch_data_from_api(date):
    formatted_date = date.strftime('%Y-%m-%d')
    response = requests.get(f"https://tradestie.com/api/v1/apps/reddit?date={formatted_date}")
    
    if response.status_code == 200 and response.content:
        try:
            data = response.json()
            return data
        except Exception as e:
            print(f"Error decoding JSON for date {formatted_date}: {e}")
            return []
    else:
        print(f"Failed to fetch data for date {formatted_date}: {response.status_code}")
        return []

def insert_data_into_db(data, date):
    # Connect to the database
    db = mysql.connector.connect(
        host=LOCAL_MYSQL_HOST,
        user="root",
        password=LOCAL_MYSQL_PASSWORD,
        database="stock_data"
    )
    cursor = db.cursor()

    # Insert data into the database
    for record in data:
        cursor.execute("SELECT COUNT(*) FROM reddit_data WHERE date = %s AND ticker = %s", (date, record['ticker']))
        result = cursor.fetchone()
        if result[0] == 0:
            cursor.execute("INSERT INTO reddit_data (date, no_of_comments, sentiment, sentiment_score, ticker) VALUES (%s, %s, %s, %s, %s)", (date, record['no_of_comments'], record['sentiment'], record['sentiment_score'], record['ticker']))

    # Commit the transaction
    db.commit()

    # Close the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    start_date = get_last_fetched_date()
    dates = generate_dates(start_date)
    
    for date in dates:
        data = fetch_data_from_api(date)
        insert_data_into_db(data, date)
        
        # Adding a delay of 60 seconds between each API request to avoid rate limiting
        time.sleep(10)
        
        # Update the last fetched date
        update_last_fetched_date(date)
    
    print("Data insertion process completed!")
