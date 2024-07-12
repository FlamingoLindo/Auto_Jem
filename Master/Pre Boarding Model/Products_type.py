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

pre_model_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/aside/nav/ul/li[4]/a/div')
                                                  )
                       ).click()

prod_type_amount_str = get_user_input("How many types?")
prod_type_amount_int = int(prod_type_amount_str)
num = 1
for _ in range(prod_type_amount_int):
    
    new_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/main/div/form/button')
                                                    )
                        ).click()
    
    input_elements = driver.find_elements(By.CSS_SELECTOR, '.fOmNul')

    num_elements = len(input_elements)

    type_input = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div/main/div/form/article[{num_elements}]/input')
                                                    )
                        ).send_keys(f"Tipo de produto automático {num}")
    
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/main/div/div/button[1]')
                                                    )
                        ).click()
    
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/main/div/div[2]/main/button')
                                                        )
                            ).click()
    num += 1

driver.quit()