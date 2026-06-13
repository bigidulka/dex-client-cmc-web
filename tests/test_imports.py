import inspect
from dex_client_cmc_web import CMCWebClient


def test_client_imports_and_instantiates():
    client = CMCWebClient()
    assert client is not None


def test_public_methods_present():
    methods = [name for name, value in inspect.getmembers(CMCWebClient, inspect.isfunction) if not name.startswith('_')]
    assert set(['listing', 'search_by_ticker', 'detail', 'detail_lite', 'quote_latest', 'market_pairs', 'exchange_pair_info', 'chart', 'historical', 'news', 'news_tldr', 'chart_annotation', 'coin_treasury', 'top_boost_listing', 'whitepaper_summary']) <= set(methods)
