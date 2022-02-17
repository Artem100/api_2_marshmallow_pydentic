from marshmallow import Schema, fields, post_load, validates
import logging
from src.schemas.news_feed_model import NewsFeedModel


class NewsFeedSchema(Schema):

        title = fields.Str()
        body = fields.Str()
        userId = fields.Int()

class NewsFeedSchemaResponse(Schema):

        id = fields.Int()
        title = fields.Str()
        body = fields.Str()
        userId = fields.Int()

        # @validates("body")
        # def validate_quantity(self, value, **kwargs):
        #         try:
        #                 assert value == kwargs
        #         except AssertionError as e:
        #                 logging.error(f"Incorrect value:")
        #                 assert False, f"Incorrect value:"