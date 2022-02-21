from pydantic import ValidationError

from src.api_response_actions import ResponseActions
from src.api_services.news_feeds import post_news, feed_json
from src.models.news_feed import NewsFeedModel
from src.schema.news_feed import NewsFeedRequest, NewsFeedResponse


def test_03(data):
    some_json = feed_json(title=data.title, body=data.body, userId=data.userId)
    response = post_news(body=some_json)
    ResponseActions().status_code_check(response, expected_code=201)
    ResponseActions().check_value_by_path(response, "title", data.title)
    ResponseActions().check_value_by_path(response, "body", data.body)
    ResponseActions().check_value_by_path(response, "userId", data.userId)
    ResponseActions().check_value_more_null(response, "id")

def test_01_pydentic(data):
    model = NewsFeedModel(title=data.title, body=data.body, userId=data.userId)
    some_json = NewsFeedRequest.from_orm(model)
    response = post_news(body=some_json)
    ResponseActions().status_code_check(response, expected_code=201)
    try:
        NewsFeedResponse(**response.json())
    except ValidationError as exc:
        print(exc)
    ResponseActions().schema_validate(response, NewsFeedResponse)

