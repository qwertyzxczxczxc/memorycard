from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
 
app = QApplication([])
 
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(700, 500)
 
# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика/n-Всего вопросов: ', window.total, '/n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100, '%'))


    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100, '%'))
def show_correct(res):
    lb_Result.setText(res)
    show_result()

def next_question():
    window.total += 1
    print('Статистика/n-Всего вопросов: ', window.total, '/n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)


question_list = []
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
question_list.append(q1)

q2 = Question('Государственный язык Франции', 'Французкий', 'Бразильский', 'Испанский', 'Итальянский')
question_list.append(q2)

q3 = Question('В каком году основана Москва', '1147', '1100', '1256', '1550')
question_list.append(q3)

q4 = Question('Какая фамилия у призидента России? ', 'Путин', 'Не Путин', 'Обама', 'Иванов')
question_list.append(q4)

q5 = Question('Что надо делать по утрам после пробуждения?', 'чистить зубы', 'Обедать', 'Ужинать', 'Лечь снова спать')
question_list.append(q5)

q6 = Question('Как правильно?', 'Ксяоми', 'Сяоми', 'СяомИ', 'Самсунг')
question_list.append(q6)

q7 = Question('С чем вкуснее пельмени?', 'Со сметаной', 'С майонезом', 'Ни с чем', 'Ни с чем')
question_list.append(q7)

q8 = Question('Зимой и летом одним цветом', 'Елка', 'Дуб', 'Сосна', 'Яблоня')
question_list.append(q8)

q9 = Question('Висит груша нельзя скушать', 'Лампочка', 'Груша', 'Яблоко', 'Что то еще')
question_list.append(q9)

q10 = Question('В каком году основан Санкт питербург', '1703', '1100', '1256', '1550')
question_list.append(q10)

def start_test():
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()
    
btn_OK.clicked.connect(start_test)

window.score = 0
window.total = 0
next_question()

window.setLayout(layout_card)
window.show()
app.exec()
