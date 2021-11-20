from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string


def generate_random_string(length):
    if length == -1: length = random.randint(10, 31)
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

#Config
message = "Test Spam" #Spam Message
gen_random_string = True #If True bot will gen a random message every time else use a string from variable message
random_string_length = -1 #Length of random string, if it is -1 bot will gen string with random size(10 - 30) characters
delay_seconds = 0.1 #Wait before send a new message

#Web
driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')
input("Auth web whatsapp session(QR code) and select chat to spam")
passed = False

while not passed:
    try:
        message_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        print(message_input)
        passed = True
    except:
        input("Error,  please select chat to spam and then press ENTER")
        passed = False
print("OK")
while True:
    if gen_random_string: message = generate_random_string(random_string_length)
    message_input.send_keys(message)
    message_input.send_keys(Keys.RETURN)
    sleep(delay_seconds)
