import customtkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import random
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/form/button')
                                                  )
                       ).click()

time.sleep(1)

contacts_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/aside/nav/ul/li[6]/a/div')
                                                  )
                       ).click()

phone_amount_str = get_user_input("How many phone numbers?")
phone_amount_int = int(phone_amount_str)
for _ in range(phone_amount_int):
    
    new_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/main/form/div[2]/button[2]')
                                                    )
                        ).click()
    
    input_elements = driver.find_elements(By.CSS_SELECTOR, '.ihmfWy')

    num_elements = len(input_elements)

    dd_input = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div/main/form/div[1]/div[3]/div[{num_elements}]/div/div[1]/div/input')
                                                    )
                        ).send_keys(11)
    
    random_num = random.randint(111111111, 999999999)

    phone_input = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div/main/form/div[1]/div[3]/div[{num_elements}]/div/div[2]/div/input')
                                                    )
                        ).send_keys(random_num)
    
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/main/form/div[2]/button[1]')
                                                    )
                        ).click()
    
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/main/form/div[3]/main/button')
                                                        )
                            ).click()

driver.quit()