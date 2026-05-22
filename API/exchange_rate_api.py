import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class ExchangeRateApi:
   # BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

    @staticmethod
    def get_exchange_rate(currency):
        try:
            API_KEY = os.getenv("EXCHANGE_API_KEY")
            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
            response = requests.get(url)
            print(response.text)
            data = response.json()
            if data["result"] != "success":
                logger.error("ExchangeAPI returned failure")
                return None
            rate= data["conversion_rates"].get(currency)
            logging.info(f"Exchange rate fetched for {currency}")
            return rate
        except Exception as e:
            logging.error(f"Exchange API failed: {e}")
            return None