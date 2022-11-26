from api import PetFriends
from settings import valid_email, valid_password
import os
from api import PetFriends
from settings import (valid_email,
                      valid_password,
                      not_valid_email,
                      not_valid_password)

pf = PetFriends()

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
def test_get_api_key_for_valid_user(
    email=valid_email,
    password=valid_password
):
    """ Проверяем, что запрос api ключа возвращает статус 200 и
        в результате содержится слово key"""
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """
def test_get_api_key_for_not_valid_email_and_password(
    email=not_valid_email,
    password=not_valid_password
):
    """ Проверяем, что запрос api ключа с неверным email пользователя
        возвращает статус 403 и в результате не содержится слово key"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем, что запрос списка всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key.
        Далее, используя этот ключ, запрашиваем список всех питомцев и
        проверяем, что список не пустой.
        Доступное значение параметра filter - pf.MY_PETS, pf.ALL_PETS """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

def test_add_new_pet_with_valid_data(
    name='Суперкот',
    animal_type='кот',
    age='3',
    pet_photo_path='images/cat2.jpg'
):
    """ Проверяем, что запрос на добавление нового питомца
        с указанными параметрами выполняется успешно."""
    pet_photo_path = os.path.join(os.path.dirname(__file__), pet_photo_path)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(
        auth_key,
        name,
        animal_type,
        age,
        pet_photo_path
    )

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type


    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
def test_add_new_pet_with_empty_age(
    name='Суперкот',
    animal_type='кот',
    age='',
    pet_photo_path='images/cat2.jpg'
):
    """ Проверяем, что запрос на добавление нового питомца
        с пустым полем возраста выполняется успешно"""
    pet_photo_path = os.path.join(os.path.dirname(__file__), pet_photo_path)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(
        auth_key,
        name,
        animal_type,
        age,
        pet_photo_path
    )

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name' in result


def test_add_new_pet_with_negative_age(
    name='Василий',
    animal_type='кот',
    age='-7',
    pet_photo_path='images/cat2.jpg'
):
    """ Проверяем, что запрос на добавление нового питомца
        с отрицательным возрастом выполняется успешно"""
    pet_photo_path = os.path.join(os.path.dirname(__file__), pet_photo_path)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(
        auth_key,
        name,
        animal_type,
        age,
        pet_photo_path
    )

    assert status == 200
    assert 'name' in result


def test_add_new_pet_with_space_in_age(
    name='Джордан',
    animal_type='Доберман',
    age=' ',
    pet_photo_path='images/dog1.jpg'
):
    """ Проверяем, что запрос на добавление нового питомца
        с пустым полем возраста выполняется успешно"""
    pet_photo_path = os.path.join(os.path.dirname(__file__), pet_photo_path)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo_path)

    assert status == 200
    assert 'name' in result


def test_add_new_pet_with_incorrect_age(
    name='Армин',
    animal_type='Собака',
    age='3456',
    pet_photo_path='images/dog1.jpg'
):
    """ Проверяем, что запрос на добавление нового питомца
        с некорректным параметром возраст питомца = 3456
        выполняется успешно."""
    pet_photo_path = os.path.join(os.path.dirname(__file__), pet_photo_path)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(
        auth_key,
        name,
        animal_type,
        age,
        pet_photo_path
    )

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    assert result['age'] == age


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    _, my_pets = pf.get_list_of_pets(auth_key, pf.MY_PETS)

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем, если список своих питомцев пустой, то добавляем нового питомца,
    # и опять запрашиваем список своих питомцев
    if not my_pets['pets']:
        pf.add_new_pet(auth_key, "Котя", "Кот", "4", "images/cat2.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, pf.MY_PETS)

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    _, my_pets = pf.get_list_of_pets(auth_key, pf.MY_PETS)

    # Проверяем что статус ответа равен 200 и
    # в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in [pet['id'] for pet in my_pets['pets']]


def test_successful_update_self_pet_info(
    name='Милка',
    animal_type='Кошка',
    age=2
):
    """ Проверяем возможность обновления информации о питомце"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, pf.MY_PETS)
    if not my_pets['pets']:
        raise Exception("There is no my pets")
    pet_id = my_pets['pets'][0]['id']

    status, result = pf.update_pet_info(auth_key,
                                        pet_id,
                                        name,
                                        animal_type,
                                        age)

    # Проверяем что статус ответа = 200 и атрибуты питомца поменялись
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == str(age)


def test_rejection_update_self_pet_info_without_name(
    name='',
    animal_type='преампуль',
    age=2
):
    """ Проверяем невозможность очистить имя питомца
        путём передачи пустого поля name """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, pf.MY_PETS)
    if not my_pets['pets']:
        raise Exception("There is no my pets")
    pet_id = my_pets['pets'][0]['id']

    status, result = pf.update_pet_info(
        auth_key,
        pet_id,
        name,
        animal_type,
        age
    )

    # Проверяем что статус ответа = 200 и имя питомца не стало пустым
    assert status == 200
    assert result['name']


    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
def test_rejection_update_self_pet_info_without_animal_type(
    name='Шарик',
    animal_type='',
    age=1
):
    """ Проверяем невозможность очистить типа питомца путём
        передачи пустого поля animal_type """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, pf.MY_PETS)

    if not my_pets['pets']:
        raise Exception("There is no my pets")
    pet_id = my_pets['pets'][0]['id']

    status, result = pf.update_pet_info(
        auth_key,
        pet_id,
        name,
        animal_type,
        age
    )
    # Проверяем что статус ответа = 200 и тип питомца не пустой
    assert status == 200
    assert pet_id not in my_pets.values()
    assert result['animal_type']


def test_successful_update_self_pet_info(name='Мурка', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""
def test_succsessful_update_self_pet_info_with_spase_name(
    name=' ',
    animal_type='прекурсор собакена',
    age=1
):
    """ Проверяем возможность очистки имени питомца путём передачи пробела
        в поле name - информация перезаписывается успешно."""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    _, my_pets = pf.get_list_of_pets(auth_key, pf.MY_PETS)

    if not my_pets['pets']:
        raise Exception("There is no my pets")
    pet_id = my_pets['pets'][0]['id']

    status, result = pf.update_pet_info(
        auth_key,
        pet_id,
        name,
        animal_type,
        age
    )
    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert status == 200
    assert result['name'] == ' '


def test_add_new_pet_with_valid_data_without_foto(
    name='Василек',
    animal_type='Котейка',
    age='1'):
    """ Проверяем, что запрос на добавление нового питомца
        без фото с указанными параметрами выполняется успешно."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name,
        animal_type,
        age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_incorrect_data_without_foto(
    name='@#$%^&!*',
    animal_type='',
    age=''
):
    """ Проверяем, что запрос на добавление нового питомца
        без фото с некорректно указанными параметрами
            name задаётся спецсимволами,
            animal_type и age - пустые
        выполняется успешно."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name,
        animal_type,
        age
    )

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
def test_successful_add_foto_of_pet(
    pet_id='',
    pet_photo_path='images/cat1.jpg'):
    """Проверяем успешность запроса на добавление фото питомца по его id"""
    pet_photo_path = os.path.join(os.path.dirname(__file__), pet_photo_path)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, pf.MY_PETS)
    if not my_pets['pets']:
        raise Exception("There is no my pets")
    pet_id = my_pets['pets'][0]['id']

    status, result = pf.add_foto_of_pet(auth_key, pet_id, pet_photo_path)

    # Проверяем что статус ответа = 200 и фото питомца соответствует заданному
    assert status == 200
    assert result['pet_photo']


