from rest_framework.pagination import PageNumberPagination


class DefinePAGINATION(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
