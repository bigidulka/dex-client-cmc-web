from __future__ import annotations

from typing import Any

from .core import BaseClient, Json

class CMCWebClient(BaseClient):
    def __init__(self, *, base_url: str = "https://api.coinmarketcap.com", timeout: float = 10.0):
        super().__init__(base_url, timeout=timeout, headers={"Accept": "application/json", "Origin": "https://coinmarketcap.com", "Referer": "https://coinmarketcap.com/"})

    def listing(self, *, start: int = 1, limit: int = 100, crypto_type: str = "all", platform_id: int | None = None, sort_by: str = "market_cap", sort_type: str = "desc", extra: dict[str, Any] | None = None) -> Json:
        params: dict[str, Any] = {"start": start, "limit": limit, "sortBy": sort_by, "sortType": sort_type, "cryptoType": crypto_type}
        if platform_id is not None: params["platformId"] = platform_id
        if extra: params.update(extra)
        return self.get("/data-api/v3/cryptocurrency/listing", params=params)

    def search_by_ticker(self, ticker: str, *, limit: int = 5000) -> list[dict[str, Any]]:
        payload = self.listing(limit=limit, crypto_type="all", extra={"convert": "USD", "tagType": "all", "audited": "false"})
        q = ticker.upper()
        rows = (((payload.get("data") or {}).get("cryptoCurrencyList")) or [])
        return [r for r in rows if q in str(r.get("symbol", "")).upper() or q in str(r.get("name", "")).upper()]

    def detail(self, *, id: int | None = None, slug: str | None = None) -> Json:
        params = {"id": id} if id else {"slug": slug}
        return self.get("/data-api/v3/cryptocurrency/detail", params=params)

    def detail_lite(self, id: int) -> Json: return self.get("/data-api/v3/cryptocurrency/detail/lite", params={"id": id})
    def quote_latest(self, id: int, convert_id: int = 2806) -> Json: return self.get("/data-api/v3/cryptocurrency/quote/latest", params={"id": id, "convertId": convert_id})
    def market_pairs(self, id: int, *, start: int = 1, limit: int = 100, category: str = "all") -> Json: return self.get("/data-api/v3/cryptocurrency/market-pairs/latest", params={"id": id, "start": start, "limit": limit, "category": category})
    def exchange_pair_info(self, **params: Any) -> Json: return self.get("/data-api/v3/cryptocurrency/web/exchange-pair-info", params=params)
    def chart(self, id: int, *, interval: str = "5m", range: str = "1D", convert_id: int = 2806) -> Json: return self.get("/data-api/v3.3/cryptocurrency/detail/chart", params={"id": id, "interval": interval, "range": range, "convertId": convert_id})
    def historical(self, id: int, *, time_start: str | None = None, time_end: str | None = None, convert_id: int = 2806, interval: str = "daily") -> Json: return self.get("/data-api/v3.1/cryptocurrency/historical", params={"id": id, "timeStart": time_start, "timeEnd": time_end, "convertId": convert_id, "interval": interval})
    def news(self, crypto_id: int, *, language: str = "en", mode: str = "top") -> Json: return self.get("/aggr/v3/news/cdp", params={"mode": mode, "cryptoId": crypto_id, "language": language})
    def news_tldr(self, slug: str, *, language_code: str = "en") -> Json: return self.post("/content/v3/news-tldr/list", json_body={"slug": slug, "languageCode": language_code})
    def chart_annotation(self, id: int, **params: Any) -> Json: return self.get("/data-api/v3/chart-annotation", params={"id": id, **params})
    def coin_treasury(self, id: int, **params: Any) -> Json: return self.get("/data-api/v3/coin-treasury/table", params={"id": id, **params})
    def top_boost_listing(self, **params: Any) -> Json: return self.get("/data-api/v3/unified-trending/top-boost/listing", params=params)
    def whitepaper_summary(self, slug: str, language: str = "en") -> Json: return self.get(f"https://s3.coinmarketcap.com/whitepaper/summaries/{slug}/{language}.json")
