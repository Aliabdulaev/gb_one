personal_data = {
    'name': input('Введите Имя - '),
    'lastname': input('Введите Фамилию - '),
    'year_of_birth': input('Введите Год Рождения - '),
    'city': input('Введите Город проживания - '),
    'email': input(' Введите email -  '),
    'phone': input('Введите phone - '),
}
def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f(**personal_data))
