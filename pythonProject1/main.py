def calculate_ticket_cost():
    total_cost = 0  # Инициализируем общую стоимость билетов
    discount = 0  # Инициализируем скидку

    try:
        num_tickets = int(input("Введите количество билетов: "))
        if num_tickets < 1:
            print("Количество билетов должно быть не менее 1.")
            return

        for i in range(1, num_tickets + 1):
            age = int(input(f"Введите возраст посетителя {i}: "))

            if age < 18:
                ticket_cost = 0  # Посетитель младше 18 лет - бесплатно
            elif 18 <= age < 25:
                ticket_cost = 990  # Посетитель от 18 до 24 лет
            else:
                ticket_cost = 1390  # Посетитель старше 24 лет

            total_cost += ticket_cost  # Добавляем стоимость билета к общей стоимости

        if num_tickets > 3:
            discount = total_cost * 0.1  # Применяем скидку 10% при покупке более 3 билетов

        total_cost -= discount  # Вычитаем скидку из общей стоимости

        print(f"Общая стоимость билетов: {total_cost} руб.")

    except ValueError:
        print("Ошибка: Введите корректный возраст и количество билетов (целое положительное число).")


if __name__ == "__main__":
    calculate_ticket_cost()
