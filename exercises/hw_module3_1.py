# 7 липня 2024 року українська спортсменка Ярослава
# Магучіх встановила світовий рекорд по стрибках у висоту –
# 2.10 метра
# Користувач вводить результат спортсмена по стрибках у
# висоту. Виведіть на екран чи вдалось побити рекорд
# Магучіх. Якщо результат такий самий то вивести фразу
# “рекорд повторено”


result_jump = float(input("Enter the result of the athlete: "))

record = 2.1

if result_jump > record:
    print("CONGRATULATIONS! You bet the record!")

elif result_jump < record:
    print("Very good! But you didn't reach the record")

elif result_jump == record:
    print("Record matched!")


# Користувач вводить сигнал світлофора(колір), потрібно
# вивести на екран що робити. Розставте блоки коду у
# правильному порядку(є 2 лишні блоки) та добавте
# підписи(до лишніх блоків допишіть коментарем чому вони
# лишні)


signal = input(
    "Введіть сигнал світлофора: "
)  # you put the signal of the traffic light and name the variable

# if signal == "Можна йти": # it doesn't makes sense, it should be the inverse, the signal of the traffic light it's green
#    print("зелений")

if signal == "червоний":  # it tells that if the light is red you need to stop
    print("Зупиніться")

elif signal == "жовтий":  # if the signal is yellow you should prepare
    print("Приготуйтеся")

elif signal == "зелений":  # if the signal it's green you can go
    print("Можна йти")

# if signal == "червоний": # if it's red you can't go , not prepare
#    print("Приготуйтеся")

else:
    print(
        "Невідомий сигнал"
    )  # if the person puts another signal, which doesn't exist, it tells that it's unknown
