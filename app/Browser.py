from pytest import UsageError


class Browser:

    @staticmethod
    def Chromium(plt, headless: bool = True):
        return plt.chromium.launch(headless=headless)

    @staticmethod
    def Firefox(plt, headless: bool = True):
        return plt.firefox.launch(headless=headless)

    @staticmethod
    def Webkit(plt, headless: bool = True):
        return plt.webkit.launch(headless=headless)

    @staticmethod
    def Chrome(plt, headless: bool = True):
        return plt.chromium.launch(channel='chrome', headless=headless)


def chose_browser(plt, browser_name: str, headless: bool):
    match browser_name:
        case 'chrome':
            return Browser.Chrome(plt, headless)
        case 'chromium':
            return Browser.Chromium(plt, headless)
        case 'firefox':
            return Browser.Firefox(plt, headless)
        case 'webkit':
            return Browser.Webkit(plt, headless)
        case _:
            raise UsageError('Wrong argument --browser. Please, chose "chrome", '
                             '"chromium", "firefox" or "webkit" (can several)')
