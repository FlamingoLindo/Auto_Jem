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

driver.get(os.getenv('CLIENT_URL'))

wait = WebDriverWait(driver, 5)

log_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/section[1]/header/a[1]')
                                                  )
                       ).click()


email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/main/section[2]/form/fieldset/div[1]/div/input')
                                                    )
                         ).send_keys(os.getenv("CLIENT_LOGIN"))

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/main/section[2]/form/fieldset/div[2]/div/input')
                                                       )
                            ).send_keys(os.getenv("CLIENT_PASSWORD"))

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/main/section[2]/form/button')
                                                  )
                       ).click()

time.sleep(1)

close_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div/div/div/div/button')
                                                  )
                       ).click()

tracking_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/aside/nav/ul/li[3]/a/div')
                                                  )
                       ).click()

track_choice = get_user_input("Insert one of the three CTe keys")

tracking_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/main/div/section/form/div[1]/div[1]/div/div')
                                                  )
                       ).click()

track_click = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(text(), 'CTe JEM')]")
        )
                             ).click()

cte_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/main/div/section/form/div[1]/div[2]/div/input')
                                                  )
                       ).send_keys(track_choice)

search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/main/div/section/form/button')
                                                  )
                       ).click()

time.sleep(1234565734)

driver.quit()