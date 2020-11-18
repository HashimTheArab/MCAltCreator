from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import os, string, random

os.system('color A')

geckopath = "./geckodriver.exe"

aclink = 'https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1605407946&rver=7.0.6738.0&wp=MBI_SSL&wreply=https:%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin%3Fru%3Dhttps%253A%252F%252Faccount.microsoft.com%252F%253Frefp%253Dsignedout-index&lc=1033&id=292666&lw=1&fl=easi2&mkt=en-US'
chars = string.ascii_letters
pswd = ''.join(random.choice(chars) for i in range(12))
email = ""
print('Please wait while Firefox opens.\n')
browser = webdriver.Firefox(executable_path=geckopath)
wait = WebDriverWait(browser, 15)
actions = ActionChains(browser)

print("""______     _                  ___  _ _     _____                _             
| ___ \   (_)                / _ \| | |   /  __ \              | |            
| |_/ / __ _ _ __ ___  ___  / /_\ \ | |_  | /  \/_ __ ___  __ _| |_ ___  _ __ 
|  __/ '__| | '_ ` _ \/ __| |  _  | | __| | |   | '__/ _ \/ _` | __/ _ \| '__|
| |  | |  | | | | | | \__ \ | | | | | |_  | \__/\ | |  __/ (_| | || (_) | |   
\_|  |_|  |_|_| |_| |_|___/ \_| |_/_|\__|  \____/_|  \___|\__,_|\__\___/|_|   
                                                                            """)

def savelogin():
    global email
    browser.get('https://temp-mail.org/en/')
    wait.until(EC.visibility_of_element_located((By.ID, 'click-to-refresh')))
    browser.find_element_by_id('click-to-refresh').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'mail')))
    email = input('Input the email from temp-mail: ')

def createmc():
    browser.get(aclink)
    wait.until(EC.visibility_of_element_located((By.ID, 'MemberName'))).send_keys(email)
    wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()
    wait.until(EC.visibility_of_element_located((By.ID, 'PasswordInput'))).send_keys(pswd)
    wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()

    print(f"Creating an account with credentials:\nEmail: {email}\nPassword: {pswd}\n")

    rmonth = random.randint(1, 12)
    rday = random.randint(1, 26)
    ryear = random.randint(1990, 2003)

    wait.until(EC.visibility_of_element_located((By.ID, 'BirthDateCountryAccrualInputPane')))
    cntry = browser.find_element_by_id('Country')
    Select(cntry).select_by_value('US')
    mnth = browser.find_element_by_id('BirthMonth')
    Select(mnth).select_by_value(f"{rmonth}")
    day = browser.find_element_by_id('BirthDay')
    Select(day).select_by_value(f"{rday}")
    year = browser.find_element_by_id('BirthYear')
    Select(year).select_by_value(f"{ryear}")
    print(f"Birth Month set to: {rmonth}\nBirth day set to: {rday}\nBirth Year set to {ryear}\n")

    wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()

    main_window = browser.current_window_handle
    browser.execute_script("window.open(''),'_blannk'")
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://temp-mail.org/en/')
    browser.execute_script("window.scrollBy(0,500)", "")
    try:
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Microsoft account team'))).click()
    except:
        print('The email appears to not be visible on the page. Please make sure everything is there. Reload the page until the email pops up if needed.\nPress enter when the email is visible on the page.')
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Microsoft account team'))).click()
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inbox-data-content-intro')))
        code = browser.find_element_by_xpath('/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr[4]/td/span').text
        print(f"Retrieved code: {code}")
    except:
        print('Make sure all the contents on the page are visible. Press enter once you are ready to proceed.')
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inbox-data-content-intro')))
        code = browser.find_element_by_xpath('/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr[4]/td/span').text
        print(f"Retrieved code: {code}")

    browser.switch_to.window(main_window)
    browser.find_element_by_id('VerificationCode').send_keys(code)
    wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()
    file = open('logins.txt', 'a')
    file.write(f"\nEmail: {email}\nPassword: {pswd}\n\n")
    file.close()
    input("The alt has been made! Solve the captcha on this screen and you're done!\nPress enter to close.")
    choice = int(input("Choose an email provider:\n[1] TempMail\n[?]: "))

choice = int(input("Choose an email provider:\n[1] TempMail\n[?]: "))
if choice == 1:
    savelogin()
    createmc()
else:
    print('That wasnt an option idiot')
    choice = input("Choose an email provider:\n[1] TempMail\n[?]: ")
