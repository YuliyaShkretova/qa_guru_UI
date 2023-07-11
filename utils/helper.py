from selene.support.shared import browser
from selene import have
from selene import command
from selene.core.wait import Command

ads = browser.all('[id^=google_ads][id$=container__]')


class js(command.js):
    scroll_one_page = Command(
        'scroll one page',
        lambda browser: browser.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)'
        ),
    )


def remove_ads(*, amount, timeout):
    if ads.with_(timeout=timeout).wait.until(have.size_greater_than_or_equal(amount)):
        ads.perform(command.js.remove)