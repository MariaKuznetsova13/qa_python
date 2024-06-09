# qa_python
## Описание тестов на класс BooksCollector:

### test_add_new_book_two_books_added - тест проверяет, что две книги добавились, названию книги присваивается пустая строка жанра, одинаковые книги не добавляются

### test_add_new_book_two_books_negative - тест проверяет, что если название книги 0 или 41 символ, то книга не добавляется

### test_set_book_genre_books_genre_and_name_set_genre - тест проверяет, что книге можно установить жанр

### test_get_book_genre_book_name_get_genre - тест проверяет, что по названию книги можно получить ее жанр

### test_get_books_with_specific_genre_books_with_genre_get - тест проверяет вывод списка книг с определенным жанром

### test_get_books_genre_get_books_dictionary - тест проверяет получение словаря с книгами

### test_get_books_for_children_books_genre_for_children_positive - тест проверяет получение книг для детей

### test_add_book_in_favorites_book_name_added_in_favorites - тест проверяет добавление книги в избранное

### test_delete_book_from_favorites_book_name_deleted - тест проверяет удаление книги из избранного

### test_get_list_of_favorites_list_of_books_received - тест проверяет получение списка избранных книг