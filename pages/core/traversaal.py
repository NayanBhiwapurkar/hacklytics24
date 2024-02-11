import requests
import orjson
import re
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class SearchResult:
    response_text: str
    web_url: list[str]

def split_bullet_points(text: str) -> list[str]:
    split_string = re.split('\d\.+', text)
    bullet_points = [bullet_point.strip() for bullet_point in split_string]
    result = []
    for bullet_point in bullet_points:
        if not bullet_point:
            continue

        result.append(bullet_point)

    return "\n.".join(result)

def get_search_from_traversaal(query: str) -> str:
    url = "https://api-ares.traversaal.ai/live/predict"

    payload = { "query": [query] }
    headers = {
      "x-api-key": os.environ['TRAVERSAAL_API_KEY'],
      "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = orjson.loads(response.content)['data']
    return SearchResult(response_text=split_bullet_points(data['response_text']), web_url=data['web_url'])