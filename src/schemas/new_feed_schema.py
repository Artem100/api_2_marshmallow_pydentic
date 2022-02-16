from marshmallow import Schema, fields, post_load

from src.schemas.news_feed_model import NewsFeedModel


class NewsFeedSchema(Schema):

        title = fields.Str()
        body = fields.Str()
        userId = fields.Int()

        # @post_load
        # def make_news(self, data, **kwargs):
        #     return NewsFeedModel(**data)