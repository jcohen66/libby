from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .api.serializers import BookSerializer, AuthorSerializer
from graphene_django.rest_framework.mutation import SerializerMutation
from .filters import BookFilter
from .models import Book, Author

# 1. Each django object becomes a 'node' in GraphQL
class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        interfaces = (relay.Node, )

class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = []
        interfaces = (relay.Node,)

# Problem: If we update a Book, that belongs to an Author,
# we run into an issue with Django Rest Framework
# (Nested Serializer - must include a "create" and "pdate")
# Book -> Author
class BookMutation(SerializerMutation):
    class Meta:
        serializer_class = BookSerializer

class Query(ObjectType):
    book = relay.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode, filterset_class=BookFilter)
    author = relay.Node.Field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode)

class Mutation(ObjectType):
    book_mutation = BookMutation.Field()