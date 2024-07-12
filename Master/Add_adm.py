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

add_adm_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/aside/nav/ul/li[3]/a/div')
                                                  )
                       ).click()

create_adm_amount_str = get_user_input("How many users?")
create_adm_amount_int = int(create_adm_amount_str)
num = 1
for _ in range(create_adm_amount_int):
   
    add_adm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/header/div/button')
                                                  )
                       ).click()
    
    name_iput = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="new-admin-form"]/div[1]/div/input')
                                                  )
                       ).send_keys(f'Usuario {num}')
    
    email_iput = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="new-admin-form"]/div[2]/div/input')
                                                  )
                       ).send_keys(f'emailtesteauto{num}@gmail.com')
    
    sector_iput = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="new-admin-form"]/div[3]/div/input')
                                                  )
                       ).send_keys(f'Setor {num}')
    
    perms_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[4]/div[1]/div')
                                                  )
                       ).click()

    branch_click = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[2]/div/div")
        )
        ).click()
    
    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/div/button[1]')
                                                  )
                       ).click()

    password = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[1]/div/input')
                                                  )
                       ).send_keys("Ab!12345")
    
    password_conf = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/form/div[2]/div/input')
                                                  )
                       ).send_keys("Ab!12345")
    
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/div[2]/button[1]')
                                                  )
                       ).click()
    
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/main/button')
                                                  )
                       ).click()
    
    num += 1
    

driver.quit()