import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()
class TestBooksCollector:
    @pytest.mark.parametrize('name, expected', [
        ('1984', True),
        ('', False),
        ('Очень длинное название книги которое превышет 40 символов!!!!', False),
        ('A' * 40, True),
        ('A' * 41, False)
    ])

    def test_add_new_book_name_length(self, collector, name, expected):
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected


    def test_set_book_genre(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.books_genre

    def test_set_invalid_genre(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984','Несуществующий жанр')
        assert collector.get_book_genre('1984') == ''

    def test_add_duplicate_book(self, collector):
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.books_genre) == 1

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['1984']

    def test_add_to_favorites(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

    def test_remove_from_favorites(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.get_list_of_favorites_books()

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Малыш и Карлсон')
        collector.set_book_genre('Малыш и Карлсон', 'Мультфильмы')
        assert 'Малыш и Карлсон' in collector.get_books_for_children()
