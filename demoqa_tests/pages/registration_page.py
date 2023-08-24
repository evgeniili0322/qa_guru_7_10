import os.path

from selene import browser, be, by, command, have


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def pick_gender(self, value):
        browser.element(f'[value={value}] +label').click()
        return self

    def fill_user_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, value):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element(by.text(value['month'])).click()
        browser.element('.react-datepicker__year-select').click()
        (browser.element('.react-datepicker__year-select').element(f'[value="{value["year"]}"]')
            .perform(command.js.scroll_into_view).click())
        browser.element(f'.react-datepicker__day--0{value["day"]}').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def pick_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()
        return self

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(value)
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered(self, first_name, last_name, email, gender, phone_number, date_of_birth, subject,
                               hobby, picture, current_address, state, city):
        browser.element('table').all('td').even.should(have.exact_texts(
            f'{first_name} {last_name}',
            email,
            gender,
            phone_number,
            f'{date_of_birth["day"]} {date_of_birth["month"]},{date_of_birth["year"]}',
            subject,
            hobby,
            os.path.basename(picture),
            current_address,
            f'{state} {city}'
        ))
