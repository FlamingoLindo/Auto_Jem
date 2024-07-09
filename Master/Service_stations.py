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
import pyautogui
import sys
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

serv_stat_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/aside/nav/ul/li[7]/a/div')
                                                  )
                       ).click()

stations_amount_str = get_user_input("How many stations?")
stations_amount_int = int(stations_amount_str)
num = 1
for _ in range(stations_amount_int):
    
    new_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/header/div/button[2]')
                                                    )
                        ).click()
    
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[1]/div[1]/div/input')
                                                    )
                        ).send_keys(f'Empresa automática {num}')

    type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[1]/div[2]/div/div')
                                                    )
                        ).click()
    
    type_click = wait.until(EC.element_to_be_clickable((By.ID, "react-select-2-option-0")
                                                    )
                        ).click()
    
    email = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[2]/div[1]/div/input')
                                                    )
                        ).send_keys(f'emailauto{num}@gmail.com')

    dd = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[2]/div[2]/div[1]/div/input')
                                                    )
                        ).send_keys(f'11')

    random_phone = random.randint(111111111, 999999999)
    phone = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[2]/div[2]/div[2]/div/input')
                                                    )
                        ).send_keys(random_phone)

    link = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[3]/div[1]/div/input')
                                                    )
                        ).send_keys("https://www.4devs.com.br/gerador_de_cep")

    link2 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[3]/div[2]/div/input')
                                                    )
                        ).send_keys("https://www.4devs.com.br/gerador_de_cep")

    cep = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[4]/div[1]/div/input')
                                                    )
                        ).send_keys(86041650)

    number = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[6]/div[2]/div/div/input')
                                                    )
                        ).send_keys(1)
 
    lat = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[7]/div[1]/div/input')
                                                    )
                        ).send_keys(1)
    
    long = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div[7]/div[2]/div/input')
                                                    )
                        ).send_keys(1)
    
    time.sleep(1)

    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/div/button[1]')
                                                    )
                        ).click()

    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/button')
                                                    )
                        ).click()
    
    num +=1

driver.quit()