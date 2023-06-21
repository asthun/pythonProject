# Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

film = {
    "title": "Title",
    "director": "Director",
    "year": 1986,
    "budget": "Budget",
    "main_actor": "Main actor",
    "slogan": "Slogan"
}
test = list(film.values())
print(test)
print(list(film.keys()))
print(list(film.items()))