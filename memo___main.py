
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QApplication
from random import shuffle, choice  #shuffle перемішує список, choice вибирає випадковий елемент зі списку
from time import sleep
#Встановлюємо розміри вікна
card_width, card_height = 600, 500 

app = QApplication([])
#Тут має бути розмітка вікна, імпортуємо з memo___card_layout
from memo___card_layout import * #memo___card_layout повинен містити елементи інтерфейсу, такі як RadioGroupBox і AnsGroupBox
from memo___app import *
#Список радіокнопок для вибору варіантів відповіді
list_rb = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
#Клас Question представляє структуру для зберігання запитання, правильної відповіді та неправильних варіантів
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question #саме запитання
        self.answer = answer #правильна відповідь
        self.wrong_answer1 = wrong_answer1 #перша неправильна відповідь
        self.wrong_answer2 = wrong_answer2 #друга неправильна відповідь
        self.wrong_answer3 = wrong_answer3 #третя неправильна відповідь
        self.correct = 0 #лічильник правильних відповідей
        self.attemps = 0 #лічильник спроб
    #Метод викликається, якщо користувач відповів правильно
    def got_right(self):
        self.correct += 1
        self.attemps += 1
        
   #Метод викликається, якщо користувач відповів неправильно
    def got_wrong(self):
        self.attemps += 1


def menu_generation():
    if cur_q.attemps != 0: #Перевіряємо, чи були спроби відповісти на питання
        result = (cur_q.correct/cur_q.attemps) * 100 #Обчислюємо відсоток правильних відповідей
    else: #Якщо спроб ще не було, успішність 0%
        result = 0
    #Формуємо текстову статистику для відображення
    text = f"Разів відповіли {cur_q.attemps}\n"\
           f"Вірних відповідей {cur_q.correct}\n"\
           f"Успішність {round(result, 2)} %"
    #Встановлюємо сформований текст у відповідний віджет статистики
    lb_statistic.setText(text)
    window_card.hide() #Ховаємо вікно картки з питанням
    menu_win.show() #Показуємо головне меню
      
def back_to_menu():
    menu_win.hide() #Ховаємо головне меню
    window_card.show() #Повертаємося до вікна картки з питанням


# Функція перемикання екрану між режимами "Вибір відповіді" та "Результат"
def swich_sceen():

    if btn_next.text() == "Відповісти": #Якщо текст кнопки "Відповісти"
        check_result()
        RadioGroupBox.hide() #Приховуємо групу з радіокнопками
        AnsGroupBox.show() #Показуємо групу з правильною відповіддю
        btn_next.setText("Наступне питання") #Змінюємо текст кнопки
    else:  #Якщо текст кнопки "Наступне питання"
        new_question()
        RadioGroupBox.show() #Показуємо групу з радіокнопками
        AnsGroupBox.hide()  #Приховуємо групу з правильною відповіддю
        btn_next.setText("Відповісти") #Змінюємо текст кнопки
#Функція для завантаження нового запитання
def new_question():

    global cur_q
    shuffle(list_rb) #Перемішуємо список радіокнопок
    cur_q = choice(list_questions) #Випадково вибираємо запитання зі списку
    lb_Correct.setText(cur_q.answer) #Встановлюємо правильну відповідь у відповідний QLabel
    lb_Question.setText(cur_q.question) #Встановлюємо текст запитання
    
    shuffle(list_rb)
    list_rb[1].setText(cur_q.wrong_answer1)  #Встановлюємо текст першої неправильної відповіді
    list_rb[2].setText(cur_q.wrong_answer2) #Встановлюємо текст другої неправильної відповіді
    list_rb[3].setText(cur_q.wrong_answer3) # Встановлюємо текст третьої неправильної відповіді
    list_rb[0].setText(cur_q.answer)  #Встановлюємо текст правильної відповіді на одну з кнопок
    shuffle(list_rb)
#Функція check_result виводить результати відповіді Правильно або не правильно
def check_result():
    for radio_button in list_rb:
        if radio_button.isChecked():
            if radio_button.text() == lb_Correct.text():
                lb_Result.setText("Правильно!")#виводиться надпис Правильно
                cur_q.got_right()
                radio_button.setChecked(False)
            else:
                lb_Result.setText("Не правильно")#виводиться надпис Не правильно
                cur_q.got_wrong()
                radio_button.setChecked(False)
check_result()
def clear():
    #Очищаємо поля вводу
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),le_wrong_ans1.text(),le_wrong_ans2.text(),le_wrong_ans3())
    list_questions.append(new_q)
    clear()
def rest():
    window_card.hide() #Ховаємо вікно картки (наприклад, робимо паузу перед наступним питанням)
    n = sp_rest.value() #Отримуємо значення часу відпочинку з віджета sp_rest
    sleep(n) #Призупиняємо виконання програми на n секунд
    window_card.show() #Після паузи знову показуємо вікно картки

    

#Створюємо запитання
q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

# Список запитань
list_questions = [q1, q2, q3, q4]
#Прив'язуємо клік на кнопку "Наступне питання" до функції перемикання екрану
new_question()
btn_clear.clicked.connect(clear)
btn_next.clicked.connect(swich_sceen)
btn_rest.clicked.connect(rest)
btn_rest.clicked.connect(menu_generation)
btn_rest.clicked.connect(back_to_menu)
btn_add_question.clicked.connect(add_question)
menu_win.show()
    
#Запускаємо додаток
app.exec_()