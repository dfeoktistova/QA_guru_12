from selene import browser, by, have
import os


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('[class="react-datepicker__month-select"]')
        self.year_of_birth = browser.element('[class="react-datepicker__year-select"]')
        self.day_of_birth = browser.element('[class="react-datepicker__day react-datepicker__day--011"]')
        self.subjects = browser.element('#subjectsInput')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.close_button = browser.element('#closeLargeModal')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.click().type(value)

    def fill_email(self, value):
        self.user_email.click().type(value)

    def select_gender(self, value):
        browser.element(by.text(value)).click()

    def fill_user_number(self, value):
        self.user_number.click().type(value)

    def select_date_of_birth(self, month, year):
        self.date_of_birth.click()

        self.year_of_birth.click().element(by.text(year)).click()
        self.month_of_birth.click().element(by.text(month)).click()
        self.day_of_birth.click()

    def fill_subjects(self, value):
        self.subjects.click().type(value).press_enter()

    def select_hobbies(self, value):
        browser.element(by.text(value)).click()

    def upload_picture(self, picture):
        path = os.path.dirname(os.path.abspath(__file__))
        self.picture.set_value(os.path.abspath(f'{path}/../resources/{picture}'))

    def fill_address(self, value):
        self.address.click().type(value)

    def select_state(self, value):
        self.state.click().element(by.text(value)).click()

    def select_city(self, value):
        self.city.click().element(by.text(value)).click()

    def submit(self):
        self.submit_button.click()

    def should_have_registered(self, first_name, last_name, email, gender, user_number, birth_day, birth_month,
                               birth_year, subjects, picture, address, state, city):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element("[class='table-responsive']").should(have.text(f'{first_name} {last_name}'))
        browser.element("[class='table-responsive']").should(have.text(email))
        browser.element("[class='table-responsive']").should(have.text(gender))
        browser.element("[class='table-responsive']").should(have.text(user_number))
        browser.element("[class='table-responsive']").should(have.text(f'{birth_day} {birth_month},{birth_year}'))
        browser.element("[class='table-responsive']").should(have.text(subjects))
        browser.element("[class='table-responsive']").should(have.text(picture))
        browser.element("[class='table-responsive']").should(have.text(address))
        browser.element("[class='table-responsive']").should(have.text(f'{state} {city}'))
