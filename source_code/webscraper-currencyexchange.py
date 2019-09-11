import requests
from bs4 import BeautifulSoup
URL1 = 'https://www.goodreturns.in/currency/world-currencies-vs-indian-rupee-inr.html'
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
 
r = requests.get(URL1, headers=headers) #get the requests from website and store unicode in variable

soup = BeautifulSoup(r.content, "lxml") # soupify the content of variable r

def livecurrencyexchange():       
    ls = soup.findAll("table", {"class": "moneyweb-currency-table"})
    currency1 = []
    cur = []
    currencyDict = {}
    for row in ls:
        currency = row.get_text()
        currency1 = currency.replace("\t", "").strip().split("\n")
        cur = currency1[4]
        name = currency1[1]
        key = name+"-"+cur[2:5]
        val = float(cur[8:11])
        currencyDict[key] = val
# take amount input from user
    INR = float(input("Enter Amount(INR):"))
    print('\n')
    print('Enter the name of the currency you want to convert amount to? Available options:\n')
    for item in currencyDict.keys():
        print(item)

    print('\n')
    currency = input('Please enter one of them: ')
    #price conversion calculation
    print(f"{INR} INR is equal to {INR*currencyDict[currency]} {currency}")
    ab = input("You want to more exchanges(Y/N): ")
    if(ab == 'Y' or ab == 'y' or ab == 'YES' or ab == 'Yes' or ab=='yes'):
        print('\n')
        livecurrencyexchange()
    else:
        exit()

livecurrencyexchange()

