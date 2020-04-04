import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions

if not os.path.exists("ogp"):
    os.mkdir("ogp")

PATHS = {
    "/?dummy": (959, 500),
    "/cards/details-of-confirmed-cases": (959, 500),
    "/cards/number-of-confirmed-cases": (959, 500),
    "/cards/attributes-of-confirmed-cases": (959, 480),
    "/cards/number-of-tested": (959, 540),
    "/cards/number-of-reports-to-covid19-telephone-advisory-center": (959, 500),
    #"/cards/number-of-reports-to-covid19-consultation-desk": (959, 500),
    #"/cards/predicted-number-of-toei-subway-passengers": (959, 750),
    "/cards/agency": (959, 730),
    "/cards/details-of-tested-cases": (959, 500),
    "/cards/number-of-inspection-persons": (959, 600),
    #"/cards/shinjuku-visitors": (959, 820),
    #"/cards/chiyoda-visitors": (959, 820),
    #"/cards/shinjuku-st-heatmap": (959, 600),
    #"/cards/tokyo-st-heatmap": (959, 600)
}
options = Options()
#prefs = {"profile.managed_default_content_settings.images": 2} # no images
#options.add_experimental_option("prefs", prefs)

# CUI
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#options.add_argument('--no-sandbox')
#options.add_argument('--window-size=1200x600')


driver = webdriver.Chrome(options=options, executable_path='./chromedriver')

for lang in ("ja", "en", "zh-cn", "zh-tw", "ko", "ja-basic"):
    if not os.path.exists("ogp/{}".format(lang)):
        os.mkdir("ogp/{}".format(lang))
    for path, size in PATHS.items():
        driver.set_window_size(*size)
        driver.get(
            "http://localhost:3000{}?ogp=true".format(
                path if lang == "ja" else "/{}{}".format(lang, path)
            )
        )
        path = path.replace("/cards/", "").replace("/", "_")
        if ('heatmap' in path):
            time.sleep(20)
        driver.save_screenshot(
            "ogp/{}.png".format(
                path if lang == "ja" else "{}/{}".format(lang, path)
            )
        )
