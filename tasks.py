from RPA.Browser.Selenium import Selenium


class Coursera:        
    browser = Selenium()
    is_authenticated = False

    def open_website(self):
        self.browser.open_available_browser('https://www.coursera.org/')
        self.browser.maximize_browser_window()



    def login_to_site(self, creds):
        self.browser.click_element_if_visible('//a[text()="Log In"]')
        self.browser.input_text_when_element_is_visible('//input[@id="email"]', creds['email'])
        self.browser.input_text('//input[@id="password"]', creds['password'])
        self.browser.click_button('//button[text()="Login"]')
        
        if self.browser.wait_until_element_is_visible('//a[text()="My Learning"]'):
            self.is_authenticated = True
        else:
            self.is_authenticated = False



    def go_to_learning_tab():
        pass


    def get_courses():
        pass


    def download_course():
        pass


