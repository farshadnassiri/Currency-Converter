import requests
from cachetools import cached,TTLCache

cache=TTLCache(maxsize=200,ttl=300)

@cached(cache)
def get_exchange_rate(base_currency,target_currency):
    url=f"https://v6.exchangerate-api.com/v6/1642b8df0034c2e4dad644c2/latest/{base_currency}"
    response=requests.get(url)
    if response.status_code != 200:
        print("Please try again!")
        return None
    return  response.json()["conversion_rates"][target_currency]  

if __name__ == "__main__":
    base_currency=input("Please Enter Base Currency:")    
    target_currency=input("Please Enter target Currency:") 
    amount=float(input("Please Enter Amount:"))
    exchange_rate=get_exchange_rate(base_currency,target_currency)
    converted_amount=amount*exchange_rate
    print(f"{amount} {base_currency} is {converted_amount} {target_currency}")  

