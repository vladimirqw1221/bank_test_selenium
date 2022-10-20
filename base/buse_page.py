

class Buse():
    def __init__(self, driver):
        self.driver = driver



    """CURRENT URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("CUrrent url " + get_url)

    """Clear input """
    def clear_input(self):
        self.driver.clear()
        print("clear input")

    """Alert clouse """
    def allert_clouse(self):
        self.driver.switchTo().alert().accept()
        print("Clocse aleert")
