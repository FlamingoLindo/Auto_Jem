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

def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma1 = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    digito1 = (soma1 * 10 % 11) % 10
    cpf.append(digito1)
    
    soma2 = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    digito2 = (soma2 * 10 % 11) % 10
    cpf.append(digito2)
    
    cpf_formatado = ''.join(map(str, cpf))
    return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

def valida_cpf(cpf):
    cpf_numeros = [int(char) for char in cpf if char.isdigit()]
    
    if len(cpf_numeros) != 11:
        return False
    
    # Validar primeiro dígito
    soma1 = sum(x * y for x, y in zip(cpf_numeros[:9], range(10, 1, -1)))
    digito1 = (soma1 * 10 % 11) % 10
    if cpf_numeros[9] != digito1:
        return False
    
    # Validar segundo dígito
    soma2 = sum(x * y for x, y in zip(cpf_numeros[:10], range(11, 1, -1)))
    digito2 = (soma2 * 10 % 11) % 10
    if cpf_numeros[10] != digito2:
        return False
    
    return True

def gera_e_valida_cpf():
    while True:
        cpf = gera_cpf()
        if valida_cpf(cpf):
            return cpf

def search_fill():
    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/fieldset[1]/button')
                                                  )
                       ).click()
    
    corp_name_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/main/div/section/form/fieldset[2]/div[1]/div/input')

    input_value = corp_name_input.get_attribute('value')
    if input_value.strip() == "":
        time.sleep(2.1)
    else:
        pass

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

pre_boarding_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/aside/nav/ul/li[2]/a/div')
                                                  )
                       ).click()

boarding_amount_str = get_user_input("How many?")
boarding_amount_int = int(boarding_amount_str)
for _ in range(boarding_amount_int):
    
    cnpj1_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/fieldset[1]/div/div/input')
                                                )
                    ).send_keys("11.591.040/0006-86")
    
    search_fill()
    
    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div/button')
                                                  )
                       ).click()
    
    cnpj2_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/fieldset[1]/div/div/input')
                                                )
                    ).send_keys("11.591.040/0001-71")
    
    search_fill()
    
    next2_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div/button[2]')
                                                  )
                       )
    next2_btn.click()
    
    cnpj3_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/fieldset[1]/div/div/input')
                                                )
                    ).send_keys("33787071865 ")
    
    search_fill()
    
    next2_btn.click()
    
    merch_type_map = {
        1:"Alimento",
        2:"Brinquedos",
        3:"Caixa",
        4:"Calçado",
        5:"Cosmético",
        6:"Entrega produto",
        7:"Medicamento",
        8:"Outros",
        9:"Prod. p/ saúde",
        10:"Prod. saneante"
    }
    
    random_num2 = random.randint(1, 10)
    
    merch_type = merch_type_map[random_num2]
    
    merch_type_dropdown = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[1]/div[1]/div/div')
        )
                                     ).click()


    merch_click = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(text(), '{merch_type}')]")
        )
                             ).click()
    
    packing_type_map = {
        1:"Caixa de GLT",
        2:"Caixa de isopor",
        3:"Caixa de madeira",
        4:"Caixa de papelão",
        5:"Diversos",
        6:"Embrulho",
        7:"Malote",
        8:"Palete de madeira",
        9:"Saca",
        10:"Tambor"
    }

    packing_type = packing_type_map[random_num2]
    
    packing_type_dropdown = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[1]/div[2]/div/div')
        )
                                     ).click()

    packing_click = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(text(), '{packing_type}')]")
        )
                             ).click()
    
    random_cte_value = random.randint(1, 999999)
    
    total_CT_e_value = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[2]/div[3]/div/input')
        )
                                     ).send_keys(random_cte_value)
    
    transfer_type_map = {
        1:"Transferência base",
        2:"Coleta + transferência + entrega",
        3:"Coleta + transferência",
        4:"Transferência + entrega",
        5:"Post Jem",
        6:"Serviço novo",    
    }
    
    random_num3 = random.randint(1, 6)
    
    transfer_type = transfer_type_map[random_num3]
    
    transfer_type_drop_down = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[2]/div[4]/div/div')
        )
                                     ).click()

    transfer_click = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(text(), '{transfer_type}')]")
        )
                             ).click()
    
    branch_map = {
        1:"CGH - Congonhas",
        2:"GRU - Guarulhos",
        3:"JGR - Jaguaré",
        4:"Matriz - São Bernardo do Campo",
        5:"mestres",
        6:"Mestres",    
        7:"Rio - Metro"  
    }
    
    random_num4 = random.randint(1, 6)
    
    branch_type = branch_map[random_num4]
    
    branch_type_drop_down = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[2]/div[5]/div/div')
        )
                                     ).click()

    branch_click = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(text(), '{branch_type}')]")
        )
                             ).click()
    
    random_vol = random.randint(1, 999)
    vol_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[3]/section/div[1]/div/input')
        )
                                     ).send_keys(random_vol)
    
    random_weight = random.randint(1, 999)
    weight_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[3]/section/div[2]/div/input')
        )
                                     ).send_keys(random_weight)
    
    random_witdh = random.randint(1, 999)
    witdh_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[3]/section/div[3]/div/input')
        )
                                     ).send_keys(random_witdh)
    
    random_hight = random.randint(1, 999)
    height_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[3]/section/div[4]/div/input')
        )
                                     ).send_keys(random_hight)
    
    random_lenght = random.randint(1, 999)
    lenght_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[3]/section/div[5]/div/input')
        )
                                     ).send_keys(random_lenght)
    
    send_rand_values = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[3]/section/button')
        )
                                     ).click()
    
    time.sleep(1)
    
    key_map = {
        1: 35240411591040000171570010039163261043781377,
        2: 35240411591040000171570010039163481074162153,
        3: 35240411591040000171570010039163191066302403,
    }
    
    random_num5 = random.randint(1, 3)
    
    key_type = key_map[random_num5]
    key_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[4]/div/div/input')
        )
                                     ).send_keys(key_type)
    
    add_key = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/form/div[4]/button')
        )
                                     ).click()
    
    generate = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Gerar')]")
        )
                                     ).click()

    time.sleep(7)

    select_card = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/section/section/article[2]/div/div/label[1]')
        )
                                     ).click()
    
    proc3ed = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Prosseguir para pagamento')]")
        )
                                     ).click()

    card_num = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="credit-card-form"]/fieldset/div[1]/div[1]/div/input')
        )
                                     ).send_keys("5428 2121 8674 0043")    

    card_name = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="credit-card-form"]/fieldset/div[2]/div/input')
        )
                                     ).send_keys("NOME")
    
    cpf_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="credit-card-form"]/fieldset/div[3]/div/input')
        )
                                     ).send_keys(gera_e_valida_cpf())

    card_val = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="credit-card-form"]/fieldset/div[4]/div/input')
        )
                                     ).send_keys("07/26")

    card_cvv = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="credit-card-form"]/fieldset/div[5]/div/input')
        )
                                     ).send_keys("985")
    
    next_btn = card_name = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div/main/div/div/button')
        )
                                     ).click()
    
    time.sleep(2)
    
    new_btn = card_name = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="modal-root"]/div/main/div[2]/button[1]')
        )
                                     ).click()

# Close the browser
driver.quit()
