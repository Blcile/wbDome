from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.db import connection

class ShowSQLMiddleware(MiddlewareMixin):
    """
    打印数据库操作
    """
    def process_respon(self, request, response):
        if settings.DEBUG:
            for query in connection.queries:
                print('[%s]:%s' % (query['time'],' '.join(query['sql'].split())))
        return response