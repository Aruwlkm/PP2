movies = [
    {"name_ru": "Кочевники", "name_kz": "Көшпенділер", "imdb": 7.1, "category_ru": "Исторический", "category_kz": "Тарихи"},
    {"name_ru": "Томирис", "name_kz": "Томирис", "imdb": 7.5, "category_ru": "Исторический", "category_kz": "Тарихи"},
    {"name_ru": "Жаужүрек мың бала", "name_kz": "Жаужүрек мың бала", "imdb": 7.3, "category_ru": "Боевик", "category_kz": "Экшн"},
    {"name_ru": "Дорога к матери", "name_kz": "Анаға апарар жол", "imdb": 8.0, "category_ru": "Драма", "category_kz": "Драма"},
    {"name_ru": "Бизнес по-казахски", "name_kz": "Бизнес по-казахски", "imdb": 6.2, "category_ru": "Комедия", "category_kz": "Комедия"},
    {"name_ru": "Кыз Жибек", "name_kz": "Қыз Жібек", "imdb": 8.5, "category_ru": "Мелодрама", "category_kz": "Мелодрама"},
    {"name_ru": "Култегин", "name_kz": "Күлтегін", "imdb": 6.8, "category_ru": "Анимация", "category_kz": "Анимация"},
    {"name_ru": "Амре", "name_kz": "Әміре", "imdb": 7.4, "category_ru": "Биография", "category_kz": "Өмірбаян"},
    {"name_ru": "Айка", "name_kz": "Айка", "imdb": 6.9, "category_ru": "Драма", "category_kz": "Драма"},
    {"name_ru": "Старик", "name_kz": "Шал", "imdb": 7.0, "category_ru": "Драма", "category_kz": "Драма"},
    {"name_ru": "Братья", "name_kz": "Ағайынды", "imdb": 6.4, "category_ru": "Криминал", "category_kz": "Криминал"},
    {"name_ru": "Рэкетир", "name_kz": "Рэкетир", "imdb": 7.1, "category_ru": "Криминал", "category_kz": "Криминал"},
    {"name_ru": "Формула любви", "name_kz": "Формула махаббат", "imdb": 6.0, "category_ru": "Романтика", "category_kz": "Романтика"},
    {"name_ru": "Султан Бейбарс", "name_kz": "Сұлтан Бейбарыс", "imdb": 7.8, "category_ru": "Исторический", "category_kz": "Тарихи"},
    {"name_ru": "16 девушек", "name_kz": "16 қыз", "imdb": 5.9, "category_ru": "Комедия", "category_kz": "Комедия"}
]


def is_above_55(movie):
    return movie["imdb"] > 5.5


def above_55_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]


def movies_by_category(movies, category, lang="ru"):
    key = "category_ru" if lang == "ru" else "category_kz"
    return [m for m in movies if m[key] == category]


def average_score(movies):
    return sum(m["imdb"] for m in movies) / len(movies)


def average_category_score(movies, category, lang="ru"):
    cat_movies = movies_by_category(movies, category, lang)
    return average_score(cat_movies) if cat_movies else 0
print( is_above_55(movies[0]))
print([m["name_ru"] for m in above_55_movies(movies)])
print([m["name_ru"] for m in movies_by_category(movies, "Драма")])
print(average_score(movies))
print(average_category_score(movies, "Исторический"))