from allure_commons._allure import step

from src.api_methods import post_method


def feed_json(title=None, body=None, userId=None):
    body = {
            "title": title,
            "body": body,
            "userId": userId,
            }
    return body

@step
def post_news(user=None, body=None):
    response = post_method("posts", user_cookies=user, json=body)
    return response