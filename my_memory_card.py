from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup)
from random import shuffle
from random import randint
#создание элементов интерфейса
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_l = list()
question_l.append(Question('Где был создан Фашизм?', 'Италия','Германия', 'Франция', 'СССР') )
question_l.append(Question('Когда был подписан пакт "Молотова Риббентропа"?', '23 августа 1939','25 февраля 1943', '15 ноября 1918', '31 декабря 1946'))
question_l.append(Question('Какое государство Германия атаковала 1 сентября 1939 года? ', 'Польша', 'Италия', 'Франция', 'Чехословакия'))


app = QApplication([])


btn_OK = QRadioButton('Ответить')
lb_Question = QLabel('Вопросы по II Мировой Войне.')


RadioGroupBox = QGroupBox('Варианты ответа')

a1 = QRadioButton('Вариант 1') 
a2 = QRadioButton('Вариант 2') 
a3 = QRadioButton('Вариант 3') 
a4 = QRadioButton('Вариант 4') 

RadioGroup = QButtonGroup()
RadioGroup.addButton(a1)
RadioGroup.addButton(a2)
RadioGroup.addButton(a3)
RadioGroup.addButton(a4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(a1)
layout_ans2.addWidget(a2)
layout_ans3.addWidget(a3)
layout_ans3.addWidget(a4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты ответа')
lb_Result = QLabel('прав или нет?')
lb_Correct = QLabel('ответ будет тута')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Cледующй вопрос')
    
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [a1, a2, a3, a4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Верно!')
        window.score += 1
        print('Статистика\п-Всего вопросов:', window.total, '\п-Правильных ответов:', window.score)
        print('Рейтинг:' , (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    window.total += 1
    print('Статистика\п-Всего вопросов:', window.total, '\п-Правильных ответов:', window.score)
    cur_question =randint(0, len(question_l) - 1)
    q = question_l [cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()



window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('MemoCard')
window.cur_question = -1

btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()