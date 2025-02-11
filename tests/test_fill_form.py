from model.registration_page import RegistrationPage
import allure

first_name = 'Santa'
last_name = 'Claus'
email = f'{first_name}@mail.com'
user_number = '1234567890'
birth_day = '11'
birth_month = 'April'
birth_year = '2007'
gender = "Male"
subjects = 'Maths'
hobby = 'Reading'
picture = 'pic.webp'
address = 'Zamshina street, 11/5'
state = 'NCR'
city = 'Noida'


def test_fill_form(browser_management):
    registration_page = RegistrationPage()

    with allure.step("Открыть страницу регистрации"):
        registration_page.open()

    with allure.step("Заполнить поле 'first_name'"):
        registration_page.fill_first_name(first_name)

    with allure.step("Заполнить поле 'last_name'"):
        registration_page.fill_last_name(last_name)

    with allure.step("Заполнить поле 'email'"):
        registration_page.fill_email(email)

    with allure.step("Заполнить поле 'gender'"):
        registration_page.select_gender(gender)

    with allure.step("Заполнить поле 'user_number'"):
        registration_page.fill_user_number(user_number)

    with allure.step("Заполнить поля 'birth_month' и 'birth_year'"):
        registration_page.select_date_of_birth(birth_month, birth_year)

    with allure.step("Заполнить поле 'subjects'"):
        registration_page.fill_subjects(subjects)

    with allure.step("Заполнить поле 'hobby'"):
        registration_page.select_hobbies(hobby)

    with allure.step("Заполнить поле 'picture'"):
        registration_page.upload_picture(picture)

    with allure.step("Заполнить поле 'address'"):
        registration_page.fill_address(address)

    with allure.step("Заполнить поле 'state'"):
        registration_page.select_state(state)

    with allure.step("Заполнить поле 'city'"):
        registration_page.select_city(city)

    with allure.step("Подтвердить регистрацию"):
        registration_page.submit()

    with allure.step("Сравнить результаты"):
        registration_page.should_have_registered(first_name, last_name, email, gender, user_number, birth_day, birth_month,
                                                 birth_year, subjects, picture, address, state, city)


