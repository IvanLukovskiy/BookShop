from django.contrib import admin

from books.models import Books, Author, Publisher


class PriceFilter(admin.SimpleListFilter):
    title = 'Фильтр по цене'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [
            ('<300', 'до 300 рублей'),
            ('от 300 до 999', '300 - 999 рублей'),
            ('>1000', 'больше 1000 рублей')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<300':
            return queryset.filter(price__lt=300)
        if self.value() == 'от 300 до 999':
            return queryset.filter(price__gte=300).filter(price__lt=1000)
        if self.value() == '>1000':
            return queryset.filter(price__gt=1000)


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'amount',
                    'get_author', 'publisher']
    list_editable = ['publisher', 'price', 'amount']
    ordering = ['title', 'price', 'amount', 'publisher']
    filter_horizontal = ('author',)
    list_per_page = 10
    search_fields = ['title', 'price']
    list_filter = [PriceFilter]

    # construction for ManytoMany Model field to be included into
    # 'list_display' here above
    @admin.display(description='author')
    def get_author(self, obj):
        return [author.__str__() for author in obj.author.all()]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name']
    list_editable = ['last_name', 'middle_name']
    ordering = ['first_name', 'last_name', 'middle_name']
    list_per_page = 10


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_per_page = 10
