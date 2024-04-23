# qa_python

Были реализованы тесты:

1. test_add_new_book_add_one_books_successfully_added
Добавляет 1 книгу с допустимым названием и проверяет, что после этого количество книг в списке равняется 1

2. test_add_new_book_null_or_long_name_not_added
Добавляет книгу с пустым или длинным названием и проверяет, что она не добавилась

3. test_set_book_genre_existing_book_and_genre_successfully_added
Добавляет жанр существующей в списке книге и проверяет, что жанр был успешно добавлен

4. test_get_book_genre_existing_book_successfully_returned
Проверяет, что возвращается корректный жанр для существующей в списке книги

5. test_get_books_with_specific_genre_existing_genre_successfully_returned
Проверяет, что возвращается корректная книга по заданному жанру

6. test_get_books_genre_get_horror_genre_successfully_returned
Проверяет, что возвращается корректное значение списка добавленных книг

7. test_get_books_for_children_mixed_genres_returns_only_children_books
Проверяет, что среди списка книг с разными жанрами возвращаются только детские книги

8. test_add_book_in_favorites_add_existing_book_successfully_added
Добавляет существующую в списке книгу в избранное и проверяет, что она успешно добавилась

9. test_delete_book_from_favorites_delete_existing_book_successfully_deleted
Удаляет существующую в списке избранных книгу и проверяет, что она успешно удалилась

10. test_get_list_of_favorites_books_not_empty_list_successfully_returned
Проверяет, что возвращается значение непустого списка избранных книг