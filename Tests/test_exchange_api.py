from API.exchange_rate_api import ExchangeRateApi

def test_exchange_rate():
    rate = ExchangeRateApi.get_exchange_rate("EUR")
    assert rate is not None
    