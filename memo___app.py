
from PyQt5.QtWidgets import QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win = QWidget() #Створюємо головне вікно меню
#Створюємо головне вікно меню
lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть вірну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')
#Створюємо поля для введення тексту (питання та відповіді)
le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()
#Створюємо заголовок для статистики
lb_header_stat = QLabel('Статистика')
lb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold;') #Налаштовуємо стиль заголовка
#Мітка для виведення статистики
lb_statistic = QLabel()
#Створюємо макети 
#Вертикальний макет для міток (запитання та варіанти відповідей)
vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)
#Вертикальний макет для полів введення відповідей
vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)
#Горизонтальний макет для об'єднання міток і полів введення
hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)
#Створюємо кнопки
btn_back = QPushButton('Назад') #Кнопка повернення до попереднього меню
btn_add_question = QPushButton('Додати запитання') #Додавання питання
btn_clear = QPushButton('Очистити')#Очищення полів

#Горизонтальний макет для кнопок
hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)
#Головний вертикальний макет для всього вмісту вікна
vl_res = QVBoxLayout()
vl_res.addLayout(hl_question) #Додаємо блок із запитанням та варіантами відповідей
vl_res.addLayout(hl_buttons) #Додаємо кнопки додавання/очищення
vl_res.addWidget(lb_header_stat) #Додаємо заголовок статистики
vl_res.addWidget(lb_statistic) #Додаємо саму статистику
vl_res.addWidget(btn_back) #Додаємо кнопку "Назад"
#Встановлюємо макет для головного вікна меню
menu_win.setLayout(vl_res)
menu_win.resize(550, 450)#Встановлюємо розмір вікна

 