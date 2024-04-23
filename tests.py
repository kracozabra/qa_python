import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('book', ['Я', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_one_book_successfully_added(self, book, collector):
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book', ['', 'Что делать, если ваш крот хочет вас убить'])
    def test_add_new_book_null_or_long_name_not_added(self, book, collector):
        collector.add_new_book(book)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_existing_book_and_genre_successfully_added(self, collector):
        collector.add_new_book('Счастливое будущее')
        collector.set_book_genre('Счастливое будущее', 'Фантастика')
        assert collector.books_genre['Счастливое будущее'] == 'Фантастика'

    def test_get_book_genre_existing_book_successfully_returned(self, collector):
        collector.books_genre = {'Счастливое будущее': 'Фантастика'}
        assert collector.get_book_genre('Счастливое будущее') == 'Фантастика'

    def test_get_books_with_specific_genre_existing_genre_successfully_returned(self, collector):
        collector.books_genre = {
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы'
        }
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        assert 'Оно' in horror_books and len(horror_books) == 1

    def test_get_books_genre_get_horror_genre_successfully_returned(self, collector):
        collector.books_genre = {'Оно': 'Ужасы'}
        assert collector.get_books_genre() == {'Оно': 'Ужасы'}

    def test_get_books_for_children_mixed_genres_returns_only_children_books(self, collector):
        collector.books_genre = {
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы',
            'Девочка с Земли': 'Фантастика'
        }
        children_books = collector.get_books_for_children()
        assert children_books == ['Девочка с Земли']

    def test_add_book_in_favorites_add_existing_book_successfully_added(self, collector):
        collector.books_genre = {'Оно': 'Ужасы'}
        collector.add_book_in_favorites('Оно')
        assert collector.favorites == ['Оно']

    def test_delete_book_from_favorites_delete_existing_book_successfully_deleted(self, collector):
        collector.favorites = ['Оно']
        collector.delete_book_from_favorites('Оно')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_not_empty_list_successfully_returned(self, collector):
        collector.favorites = ['Оно', 'Шерлок Холмс']
        assert collector.get_list_of_favorites_books() == ['Оно', 'Шерлок Холмс']
