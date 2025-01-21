from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument("--disable-gpu")
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=option)

# End of setup

driver.get('http://saucedemo.com/')
driver.maximize_window()

# АВТОРИЗАЦИЯ НА САЙТЕ  ------------------------
file.write("    LOGIN\n")


def login():
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('standard_user')
    file.write("Success login input \n")

    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys('secret_sauce')
    file.write("Success password input \n")
    password.send_keys(Keys.ENTER)
    file.write("Success login with Enter \n")


def test_login_redirect():
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
        "test_login_redirect is FAILED"
    file.write("test_login_redirect is OK \n")


login()
test_login_redirect()


# СПИСОК ТОВАРОВ  ------------------------

def products_block():
    file.write("\n    PRODUCTS LIST\n")

    products_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

    print("Список товаров:")
    for index, product in enumerate(products_list, start=1):
        print(index, product.text)

    # Запрос ввода и обработка ошибок
    def get_selected_numbers():
        selected_numbers_input = input("Введите номера товаров через пробел:\n")

        # пустой ввод
        if not selected_numbers_input.strip():
            file.write("Empty input\n")
            return None

        # преобразуем в список, удаляем дубликаты, исключаем неверный ввод
        try:
            selected_numbers_list = list(set(map(int, selected_numbers_input.split())))
            return selected_numbers_list
        except ValueError:
            print("Ошибка: введите только числа, разделенные пробелами\n")
            return None

    # Получаем корректный ввод от пользователя
    selected_numbers_list = get_selected_numbers()
    file.write(f"selected_numbers: {selected_numbers_list}\n")

    # После корректного ввода номеров, выполняем добавление товаров в корзину
    if selected_numbers_list:
        for number in selected_numbers_list:
            if 1 <= number <= len(products_list):
                driver.find_element(By.XPATH, f'//div[@class="inventory_item"][{number}]//button').click()
                print(f"Товар {number} добавлен в корзину.")
                file.write(f"Product number {number} added to cart\n")
            else:
                print(f"Номер {number} недопустим. Пропускаем.")
                file.write(f"Invalid product number {number}\n")
    else:
        file.write("Invalid input\n")


# КОРЗИНА ------------------------

def redirect_to_shopping_cart():
    file.write("\n    SHOPPING CART\n")
    shopping_cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    shopping_cart_button.click()

    # Тест перехода в корзину:
    def test_shopping_cart_redirect():
        assert driver.current_url == 'https://www.saucedemo.com/cart.html', \
            "test_shopping_cart_redirect is FAILED"
        file.write("test_shopping_cart_redirect is OK \n")

    test_shopping_cart_redirect()
    print("\nВы перенаправлены в корзину\n")


# Основной цикл выбора действия
while True:
    # Первый вызов блока товаров
    products_block()

    # Переход в корзину
    redirect_to_shopping_cart()

    # Отображение списка товаров в корзине
    shopping_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    if not shopping_list:
        print("Корзина пуста\n")
    else:
        print("Список товаров в корзине:")
        for product in shopping_list:
            print(product.text)

    # Запрос дальнейшего действия
    while True:
        action_selection = input("\nВыберите дальнейшее действие:\n"
                                 "1. Изменить список товаров\n"
                                 "2. Оформить заказ\n"
                                 "3. Завершить программу\n")

        if action_selection == "1":
            file.write("List change selected\n")
            # Очистка корзины
            remove_buttons = driver.find_elements(By.XPATH, '//button[text()="Remove"]')
            for button in remove_buttons:
                button.click()
            print("Корзина очищена.\n")
            file.write("Shopping cart cleaned\n")

            # Возвращаемся к блоку товаров и проверяем ссылку
            driver.back()  # Возврат на предыдущую страницу
            file.write("Return to products list\n")


            def test_return_to_products_list():
                assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
                    "test_return_to_products_list is FAILED"
                file.write("test_return_to_products_list is OK\n")


            test_return_to_products_list()
            break  # Выход из внутреннего цикла для возврата к списку товаров
        elif action_selection == "2":
            file.write("Checkout selected\n")
            if not shopping_list:
                print("Ошибка заказа. Товары не выбраны\nПрограмма завершена\n")
                file.write("No products selected\nProgram finished\n")
                file.close()
                driver.quit()
                exit()  # Завершаем программу
            else:
                # Переход к оформлению заказа
                checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
                checkout_button.click()
                print("Переход к оформлению заказа.\n")
                file.write("Checkout redirect\n")


                def test_checkout_button_redirect():
                    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html', \
                        "test_checkout_button_redirect is FAILED"
                    file.write("test_checkout_button_redirect is OK\n")


                test_checkout_button_redirect()
            break  # Завершаем цикл, так как пользователь выбрал оформление заказа
        elif action_selection == "3":
            print("Программа завершена.\n")
            file.write("Program finished by user choice.\n")
            file.close()
            driver.quit()
            exit()  # Завершаем программу
        else:
            print("\nНеверный ввод. Выберите действие 1, 2 или 3")
            continue  # Повторный запрос выбора действия

    if action_selection in ["2", "3"]:
        break  # Завершаем внешний цикл, если выбрано оформление заказа или завершение программы

# ОФОРМЛЕНИЕ ЗАКАЗА ------------------------
file.write("\n    CHECKOUT\n")

# Ввод имени
while True:
    first_name = input("Введите имя: \n")
    if first_name.strip():  # Проверка на пустой ввод
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys(first_name)
        file.write("First name entered\n")
        break
    else:
        print("Имя не может быть пустым. Пожалуйста, введите имя.")

# Ввод фамилии
while True:
    last_name = input("Введите фамилию: \n")
    if last_name.strip():  # Проверка на пустой ввод
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys(last_name)
        file.write("Last name entered\n")
        break
    else:
        print("Фамилия не может быть пустой. Пожалуйста, введите фамилию.")

# Ввод почтового индекса
while True:
    postal_code = input("Введите почтовый индекс: \n")
    if postal_code.strip():  # Проверка на пустой ввод
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(postal_code)
        file.write("Postal code entered\n")
        break
    else:
        print("Почтовый индекс не может быть пустым. Пожалуйста, введите индекс.")


# Переход к информации о заказе
def continue_button_click():
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    file.write("Continue button clicked\n")

    def test_continue_button_click_redirect():
        assert driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html', \
            "test_continue_button_click_redirect is FAILED"
        file.write("test_continue_button_click_redirect is OK\n")

    test_continue_button_click_redirect()


continue_button_click()

# ПОДТВЕРЖДЕНИЕ ЗАКАЗА ------------------------
file.write("\n    ORDER OVERVIEW\n")

# Информация о заказе
print("\nИнформация о заказе:")
print("Список товаров:")
shopping_list_check = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
for product_check in shopping_list_check:
    print(product_check.text)

item_total = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]').text.replace("Item total: $", "")
tax = driver.find_element(By.XPATH, '//div[@class="summary_tax_label"]').text.replace("Tax: $", "")
price_total = driver.find_element(By.XPATH, '//div[@class="summary_total_label"]').text.replace("Total: $", "")
shipping_information = driver.find_element(By.XPATH, '//div[@class="summary_value_label"][1]').text
payment_information = driver.find_element(By.XPATH, '//div[@class="summary_value_label"][2]').text

# Вывод информации
print(f"\nСтоимость товаров: ${item_total}")
print(f"Налог: ${tax}")
print(f"Общая сумма: ${price_total}")
print(f"Информация о доставке: {shipping_information}")
print(f"Информация об оплате: {payment_information}\n")

file.write("Checkout overview displayed\n")

file.write("\n    ORDER CONFIRMATION\n")
# Запрос подтверждения заказа
while True:
    confirmation = input("\nПодтвердить заказ?\n"
                         "1. Да\n"
                         "2. Нет\n")

    if confirmation == "1":
        file.write("Confirmation selected\n")
        # Нажимаем кнопку Finish
        finish_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
        finish_button.click()
        file.write("Finish button is clicked\n")


        # Проверка перехода на страницу завершения заказа
        def test_finish_button_redirect():
            assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html', \
                "test_finish_button_redirect is FAILED"
            file.write("test_finish_button_redirect is OK\n")


        def test_context_after_finish_button_redirect():
            assert driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2').text == \
                   "Thank you for your order!", "test_context_after_finish_button_redirect if FAILED"
            file.write("test_context_after_finish_button_redirect is OK\n")


        test_finish_button_redirect()
        test_context_after_finish_button_redirect()

        file.write("Order confirmed successfully")
        print("\nЗаказ успешно оформлен!\n")
        break
    elif confirmation == "2":
        print("\nЗаказ отменен. Программа завершена.\n")
        file.write("Order canceled. Program finished.\n")
        break
    else:
        print("\nНеверный ввод. Выберите 1 или 2\n")
        continue  # Повторный запрос подтверждения

file.close()
driver.quit()
