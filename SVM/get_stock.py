import csv

import requests


def get_historical(__quote__):
    __file_name__ = "temp.csv"

    url = 'http://ichart.yahoo.com/table.csv?s=' + __quote__
    r = requests.get(url, stream=True)

    if r.status_code != 400:
        with open(__file_name__, 'wb') as f:
            for chunk in r:
                f.write(chunk)
        set_prev_close(__file_name__)
        return True


def set_prev_close(__file_name__):
    with open(__file_name__) as file:

        date = []
        close_price = []
        open_price = []
        high_price = []
        low_price = []
        volume = []

        reader = csv.DictReader(file)
        for row in reader:
            date.append(row['Date'])
            open_price.append(row['Open'])
            high_price.append(row['High'])
            low_price.append(row['Low'])
            close_price.append(row['Close'])
            volume.append(row['Volume'])

    with open(__file_name__, 'w') as __csv_file__:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close Price', 'Prev Close Price', 'Volume']
        writer = csv.DictWriter(__csv_file__, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(len(date) - 1):
            writer.writerow({'Date': date[i], 'Open': open_price[i], 'High': high_price[i], 'Low': low_price[i],
                             'Close Price': close_price[i], 'Prev Close Price': close_price[i + 1],
                             'Volume': volume[i]})
        return
