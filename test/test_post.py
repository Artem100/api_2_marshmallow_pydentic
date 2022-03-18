import jsonpath_rw

from src.api_actions.api_response_actions import ResponseActions
from src.models.news_feed import NewsFeedModel
from src.schema.feed.news_feed import NewsFeedRequest, NewsFeedResponse
from src.services.news_feeds import feed_json, post_news


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
    request_data = NewsFeedRequest.from_orm(model)

    response = post_news(body=request_data)
    model.id = ResponseActions().get_value_by_easy_jsonpath(response, "id")
    response_data_check = NewsFeedResponse.from_orm(model)
    ResponseActions().validate_data_response(response, response_data_check,
                                             expected_code=300,
                                             schema=NewsFeedResponse,
                                             exclude_paths="root['id!']")

    # Задать, что проверка или заполение поля ID не обязательно и не добавлять его в тело запроса
    # request_data = NewsFeedResponse.from_orm(model)
    # print(request_data.json())
    # ResponseActions.validate_data_response_values_with_request

