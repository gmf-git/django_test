from rest_framework.viewsets import ModelViewSet


class DefaultViewSet(ModelViewSet):
    list_serializer = None
    create_serializer = None

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return self.list_serializer
        return self.create_serializer


def get_keywords(search_map, params):
    keywords = {}
    for k, v in search_map.items():
        middle_value = params.get(v)
        if middle_value:
            keywords.setdefault(k, middle_value)
    return keywords
