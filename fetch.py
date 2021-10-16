from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def fetch(profile):
    path = r'C:\Users\ankit_y\Downloads\chromedriver_win32\chromedriver'
    driver = webdriver.Chrome(executable_path = path)
    driver.get('http://sololearn.com/Profile/'+profile)
    try:
        elem = WebDriverWait(driver, 30,poll_frequency=1).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sl-p-details__country-name"))
        )
        if elem.text:
            country = driver.find_element_by_css_selector("#main > div > div > div > div > div > div.sl-p-container__center > div.sl-p-details.dark > div.sl-p-details__info > div.sl-p-details__country-and-level.sl-p-details__row.dark > div").text
            name = driver.find_element_by_css_selector("#main > div > div > div > div > div > div.sl-p-container__center > div.sl-p-details.dark > div.sl-p-details__info > div.sl-p-details__header.sl-p-details__row > div.sl-p-details__name").text
            following = driver.find_element_by_css_selector("#main > div > div > div > div > div > div.sl-p-container__center > div.sl-p-details.dark > div.sl-p-details__info > div:nth-child(2) > button:nth-child(1)").text
            followers = driver.find_element_by_css_selector("#main > div > div > div > div > div > div.sl-p-container__center > div.sl-p-details.dark > div.sl-p-details__info > div:nth-child(2) > button:nth-child(2)").text
            level = driver.find_element_by_css_selector("#main > div > div > div > div > div > div.sl-p-container__center > div.sl-p-details.dark > div.sl-p-details__info > div.sl-p-details__country-and-level.sl-p-details__row.dark > span:nth-child(3)").text
            xp = driver.find_element_by_css_selector("#main > div > div > div > div > div > div.sl-p-container__center > div.sl-p-details.dark > div.sl-p-details__info > div:nth-child(3) > span").text
            courses = {}
            if len(driver.find_elements_by_css_selector(".sl-p-courses__show-all")) > 0:
                button = driver.find_element_by_css_selector(".sl-p-courses__show-all")
                driver.execute_script("arguments[0].click();", button)
                course_modal = driver.find_element_by_css_selector(".sl-p-all-progress-modal__body")
                course = course_modal.find_elements_by_css_selector(".sl-p-progress__body__label__name")
                completion = course_modal.find_elements_by_css_selector(".sl-p-progress__body__label__sec")
                for i,j in zip(course,completion):
                    courses[i.text] = j.text
            else:
                course = driver.find_elements_by_css_selector(".sl-p-progress__body__label__name")
                completion = driver.find_elements_by_css_selector(".sl-p-progress__body__label__sec")
                for i,j in zip(course,completion):
                    courses[i.text] = j.text

            codes = {}
            if len(driver.find_elements_by_css_selector(".sl-p-codes__show-all"))>0:
                button = driver.find_element_by_css_selector(".sl-p-codes__show-all")
                driver.execute_script("arguments[0].click();", button)
                code_modal = driver.find_element_by_css_selector(".sl-p-all-codes__body")
                code_name = code_modal.find_elements_by_css_selector(".sl-p-code-item__link__name")
                code_lang = code_modal.find_elements_by_css_selector(".sl-p-code-item__link__icon > p")
                for i,j in zip(code_name,code_lang):
                    codes[i.text] = j.text
            else:
                code_name = driver.find_elements_by_css_selector(".sl-p-code-item__link__name")
                code_lang = driver.find_elements_by_css_selector(".sl-p-code-item__link__icon > p")
                for i,j in zip(code_name,code_lang):
                    codes[i.text] = j.text
            return [xp,level,following,followers,name,country,courses,codes]

    finally:
        driver.quit()