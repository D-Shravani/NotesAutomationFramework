from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    email_input = (
        By.ID,
        "email"
    )

    password_input = (
        By.ID,
        "password"
    )

    login_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def login(self, email, password):

        wait = WebDriverWait(self.driver, 20)

        wait.until(
            EC.visibility_of_element_located(
                self.email_input
            )
        )

        self.enter_text(
            self.email_input,
            email
        )

        self.enter_text(
            self.password_input,
            password
        )

        login_btn = wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_btn
        )