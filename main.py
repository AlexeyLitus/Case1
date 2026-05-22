import json

FILENAME = 'books.json'

def load_books():
    """Загружает список книг из файла JSON. Если файла нет — возвращает пустой список."""
    with open(FILENAME, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    """Сохраняет список книг в файл JSON."""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def main():
    books = load_books()

    while True:
        print("\n--- Трекер прочитанных книг ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass            
            
        elif choice == '6':
            print(" До свидания!")
            break
        else:
            print(" Неверный пункт меню. Попробуйте ещё раз.")

    save_books(books)

if __name__ == "__main__":
    main()