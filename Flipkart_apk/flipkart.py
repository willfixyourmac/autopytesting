from appium import webdriver
import base64
import os
import time


desired_cap = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "/Users/yu/Downloads/flipkart.apk",
    "appPackage": "com.flipkart.android",
    "appWaitActivity": "com.flipkart.android.activity.MSignupActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

driver.start_recording_screen()

driver.implicitly_wait(30)

driver.find_element_by_id("com.flipkart.android:id/mobileNo").click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.flipkart.android:id/mobileNo").send_keys("6")
driver.implicitly_wait(20)
driver.find_element_by_id("com.flipkart.android:id/country_code_info").click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.flipkart.android:id/search_country_name").send_keys("Canada")
driver.implicitly_wait(20)
driver.find_element_by_id("com.flipkart.android:id/country_row_item_full_name").click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.flipkart.android:id/mobileNo").clear()
driver.find_element_by_id("com.flipkart.android:id/mobileNo").send_keys("647221413")   #entering phone number

driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.flipkart.android:id/et_password").click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.flipkart.android:id/et_password").send_keys("simnarsimnar")
driver.implicitly_wait(20)
driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()


ts = (time.strftime("%Y_%m_%d_%H%M%S"))
activityname = driver.current_activity
filename = activityname+ts

driver.save_screenshot("/Users/yu/Desktop/" + filename + ".png")



video_rawdata = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

filepath = os.path.join("/Users/yu/Desktop/", video_name + ".mp4")
with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))
