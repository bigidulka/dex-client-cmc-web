# CoinMarketCap Web Reverse Client

Python client for endpoints used by [https://coinmarketcap.com](https://coinmarketcap.com). The implementation is browser/reverse-engineered and mirrors the internal clients used in local DEX modules.

## Educational Use

This project is published as part of an educational process for studying web/API clients and data access patterns. It is unofficial, not affiliated with or endorsed by the upstream service, and should be used responsibly according to the target site's terms and applicable law.


## Install

```bash
pip install git+https://github.com/bigidulka/dex-client-cmc-web.git
```

For local development:

```bash
pip install -e '.[dev]'
pytest
```

## Quick start

```python
from dex_client_cmc_web import CMCWebClient

client = CMCWebClient()
# call any method below; all methods return decoded JSON dict/list payloads
```

## Methods

- `listing`
- `search_by_ticker`
- `detail`
- `detail_lite`
- `quote_latest`
- `market_pairs`
- `exchange_pair_info`
- `chart`
- `historical`
- `news`
- `news_tldr`
- `chart_annotation`
- `coin_treasury`
- `top_boost_listing`
- `whitepaper_summary`

## Endpoint inventory

Extracted from existing Local clients and rechecked with browser-harness network capture where the site allowed capture.

- `['GET', '/data-api/v3/cryptocurrency/listing', 'listing/search/tokens by platform']`
- `['GET', '/data-api/v3/cryptocurrency/detail', 'detail']`
- `['GET', '/data-api/v3/cryptocurrency/detail/lite', 'detail lite']`
- `['GET', '/data-api/v3/cryptocurrency/market-pairs/latest', 'market pairs']`
- `['GET', '/data-api/v3/cryptocurrency/web/exchange-pair-info', 'exchange pair info']`
- `['GET', '/data-api/v3/cryptocurrency/quote/latest', 'quote latest']`
- `['GET', '/data-api/v3.3/cryptocurrency/detail/chart', 'chart']`
- `['GET', '/data-api/v3.1/cryptocurrency/historical', 'historical']`
- `['POST', '/content/v3/news-tldr/list', 'news tldr']`
- `['GET', '/aggr/v3/news/cdp', 'news']`
- `['GET', '/content/v3/ad-banner/top', 'ad banner']`
- `['GET', '/data-api/v3/chart-annotation', 'chart annotation']`
- `['GET', '/data-api/v3/coin-treasury/table', 'treasury']`
- `['GET', '/data-api/v3/unified-trending/top-boost/listing', 'top boost']`

Full details: [`endpoint_inventory.json`](endpoint_inventory.json).

## Notes

- No official SDK is used.
- Some endpoints require Cloudflare/browser behavior; pass `use_curl_cffi=True` where available.
- Auth/session-only methods need your own cookies/tokens. Do not commit secrets.
- These clients are thin transport wrappers; normalize data in your application layer.
