from appium import webdriver
from selenium.webdriver.common.by import By


def test_changeTemperature():
    # Desired capabilities for Android device and app
    driver = initiate_driver()

    # get the temperature before the change
    previous_temperature = driver.find_element(By.ID, 'your_displayed_temperature_id').text

    change_temperature(driver)
    verify_temperature(driver, previous_temperature)
    driver.quit()


def initiate_driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '{your_android_version}',
        'deviceName': '{your_device_name}',
        'appPackage': '{your_app_package}',
        'appActivity': '{your_app_activity}'
    }

    return webdriver.Remote('http://localhost:{relevant_port}/wd/hub', desired_caps)


def change_temperature(driver):
    # Locate the temperature text box and enter a different value from previous_temperature
    temperature_text_box = driver.find_element(By.ID, 'your_temperature_text_box_id')
    temperature_text_box.clear()
    temperature_text_box.send_keys('25')


def verify_temperature(driver, previous_temperature):
    # Check if the displayed temperature matches the entered value
    current_temperature = driver.find_element(By.ID, 'your_displayed_temperature_id').text
    assert current_temperature == '25'
    assert current_temperature != previous_temperature
