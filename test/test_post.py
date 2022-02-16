from src.api_response_actions import ResponseActions
from src.api_services.news_feeds import post_news, feed_json
from src.schemas.new_feed_schema import NewsFeedSchema
from src.schemas.news_feed_model import NewsFeedModel


def test_03(data):
    some_json = feed_json(title=data.title, body=data.body, userId=data.userId)
    response = post_news(body=some_json)
    ResponseActions().status_code_check(response, expected_code=201)
    ResponseActions().check_value_by_path(response, "title", data.title)
    ResponseActions().check_value_by_path(response, "body", data.body)
    ResponseActions().check_value_by_path(response, "userId", data.userId)
    ResponseActions().check_value_more_null(response, "id")


def test_user_marsh(data):
    news = NewsFeedModel(title=data.title, body=data.body, userId=data.userId)
    schema = NewsFeedSchema()
    make_json = schema.dump(news)
    print(make_json)
    response = post_news(body=make_json)
    ResponseActions().status_code_check(response, expected_code=201)
