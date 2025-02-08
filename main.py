from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel,Field,EmailStr
import uvicorn
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY  = "cur_live_n7prexRynwmSrl47vcsywQ9qHMJRMPWVywzC4YuG"
url = f"https://api.currencyapi.com/v3/latest?apikey={API_KEY}&base_currency="
list_of_currency = [
    "USD",
    "EUR",
    "RUB",
    "GBP",
]



def url_set(currency):
    response = requests.get(url+currency)
    data = response.json()
    return data

@app.get(
    "/currency/{name}"
)
def get_convert(name: str):
    result = {}
    data = url_set(name)
    try:
        for i in data["data"].keys():
            if i in list_of_currency and i != name:
                result[i] = data["data"][i]
        return result
    except:
        raise HTTPException(status_code=404, detail="Currency not found")





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)