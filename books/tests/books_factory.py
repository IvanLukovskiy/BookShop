import factory
from factory.django import DjangoModelFactory

from books.models import Books, Author, Publisher


class PublisherFactory(DjangoModelFactory):
    class Meta:
        model = Publisher

    name = 'test_pub'


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    first_name = 'Albert'
    last_name = 'Sysoev'
    middle_name = 'Valentinovich'


class BooksFactory(DjangoModelFactory):
    class Meta:
        model = Books

    title = 'test_book'
    price = '25.00'
    amount = 30
    publisher = factory.SubFactory(PublisherFactory)

    # author = factory.SubFactory(AuthorFactory)

    @factory.post_generation
    def author(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.author.add(*extracted)
