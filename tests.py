from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    @pytest.mark.parametrize('book_name', ['', '12345678901234567890123456789012345678901'])
    def test_add_new_book_two_books_negative(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize('book_name, genre, expected_genre', [
        ['Гордость и предубеждение и зомби', 'Фантастика', 'Фантастика'],
        ['Гордость и предубеждение и зомби', 'Драма', ''],
    ])
    def test_set_book_genre_books_genre_and_name_set_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == expected_genre

    @pytest.mark.parametrize('book_name, genre, expected_genre', [
        ['Гордость и предубеждение и зомби', 'Фантастика', 'Фантастика'],
        ['Гордость и предубеждение и зомби', '', ''],
    ])
    def test_get_book_genre_book_name_get_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ['Zombies', 'Ужасы'],
            ['It', 'Ужасы'],
            ['Гордость и предубеждение и зомби', 'Фантастика']
        ])
    def test_get_books_with_specific_genre_books_with_genre_get(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    def test_get_books_genre_get_books_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Zombies')
        collector.set_book_genre('Zombies', 'Ужасы')
        assert collector.get_books_genre() == {'Zombies': 'Ужасы'}

    def test_get_books_for_children_books_genre_for_children_positive(self):
        collector = BooksCollector()

        collector.add_new_book('Zombies')
        collector.add_new_book('It')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Zombies', 'Ужасы')
        collector.set_book_genre('It', 'Ужасы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_book_name_added_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Zombies')
        collector.add_book_in_favorites('Zombies')
        collector.add_book_in_favorites('Zombies')
        assert collector.favorites == ['Zombies']

    def test_delete_book_from_favorites_book_name_deleted(self):
        collector = BooksCollector()

        collector.add_new_book('Zombies')
        collector.add_book_in_favorites('Zombies')
        collector.delete_book_from_favorites('Zombies')
        assert collector.favorites == []

    def test_get_list_of_favorites_list_of_books_received(self):
        collector = BooksCollector()

        collector.add_new_book('Zombies')
        collector.add_book_in_favorites('Zombies')
        assert collector.get_list_of_favorites_books() == ['Zombies']
