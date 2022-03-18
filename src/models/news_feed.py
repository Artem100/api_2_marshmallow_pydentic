class NewsFeedModel():

    def __init__(self, title, body, userId):
        self.title = title
        self.body = body
        self.userId = userId

class NewsModel2():

    def __init__(self):
        self.news = {}
        self.reset()

    def set_title(self, title='Some'):
        self.news['title'] = title
        return self

    def set_body(self, body="dodo"):
        self.news['body'] = body
        return self

    def set_userId(self, userId=100):
        self.news['userId'] = userId
        return self

    def build(self):
        """
        Сборка всего генератора
        :return:
        """
        return self.news

    def reset(self):
        """
        Нужно чтобы все заполнялось дефолтными значениями
        :return:
        """
        self.set_title()
        self.set_body()
        self.set_userId()

    def add_key_to_body(self, key, value):
        self.news[key] = value
        return self

z = NewsModel2().add_key_to_body("my_key", "hello").set_title("asdasd").build()
print(z)
