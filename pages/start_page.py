from pages.base_page import BasePage
from altunityrunner import By


class StartPage(BasePage):
    def __init__(self, altdriver, appium_driver):
        BasePage.__init__(self, altdriver, appium_driver)

    def load(self):
        self.altdriver.load_scene('Start')

    @property
    def start_button(self):
        return self.altdriver.find_object(By.NAME, 'StartButton')

    @property
    def start_text(self):
        return self.altdriver.find_object(By.NAME, 'StartText')

    @property
    def logo_image(self):
        return self.altdriver.find_object(By.NAME, 'LogoImage')

    @property
    def unity_url_button(self):
        return self.altdriver.find_object(By.NAME, 'UnityURLButton')

    def is_displayed(self):
        if self.start_button and self.start_text and self.logo_image and self.unity_url_button:
            return True

    def put_app_in_background(self, background_time):
        self.appium_driver.background_app(background_time)



        #myData



    @property
    def start_btn(self):
        return self.altdriver.find_object(By.NAME, 'StartButton')

    @property
    def dog_run(self):
        return self.altdriver.find_object(By.NAME, 'DogRun_Final:DogMesh')


    def is_main_page_displayed(self):
        if self.start_btn and self.dog_run:
            return True


    def dog_run_status(self):
        self.appium_driver.dog_run.tap()
        return True


