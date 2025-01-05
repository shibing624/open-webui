import logging

import requests
from open_webui.retrieval.web.main import SearchResult
from open_webui.env import SRC_LOG_LEVELS
import uuid
import json

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["RAG"])


def search_pro(api_key: str, query: str, count: int = 10) -> list[SearchResult]:
    """
    Search using ZhipuAI's web search pro API and return the results as a list of SearchResult objects.
    Args:
        query (str): The query to search for
        count (int): The number of results to return

    Returns:
        list[SearchResult]: A list of search results
    """
    if not api_key:
        raise ValueError("Please set the ZHIPUAI_API_KEY")

    log.debug(f"Searching web for: {query}")
    msg = [{"role": "user", "content": query}]
    tool = "web-search-pro"
    url = "https://open.bigmodel.cn/api/paas/v4/tools"
    data = {
        "request_id": str(uuid.uuid4()),
        "tool": tool,
        "stream": False,
        "messages": msg
    }
    resp = requests.post(
        url,
        json=data,
        headers={'Authorization': api_key},
        timeout=30
    )
    data = json.loads(resp.content.decode())
    # parse data
    search_results = data['choices'][0]['message']['tool_calls'][1]['search_result']

    results = []
    for result in search_results[:count]:
        results.append(
            SearchResult(
                link=result.get("link", ""),
                title=result.get("title"),
                snippet=result.get("content"),
            )
        )
    log.debug(f"search result: {results}")
    return results
