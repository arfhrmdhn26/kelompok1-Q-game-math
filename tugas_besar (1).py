import random
import time

from typing import List

def generate_expression(no_of_operators):
    operations = ['+', '-', '*', '/']
    expression = []

    expression.append(random.randint(0, 20))

    for _ in range(no_of_operators):
        expression.append(random.choice(operations))
        expression.append(random.randint(0, 20))

    expression = ''.join(str(term) for term in expression)
    return expression


def result(expression):
    return (int(eval(expression)))

def evaluate(solution, user_solution):
    if solution == user_solution:
        return True
    else:
        return False

    
print("""Welcome to the maths game Kelompok 1!!!
-----------------------------
Uji keterampilan aritmatika dasar Anda dengan memainkan game sederhana ini. Dengan setiap 5 jawaban yang benar, levelnya meningkat
menambah kesulitan soal.
Ingat :
----------
         1. Tulis hanya bagian integral dari jawaban
         2. Prioritas operator berlaku
         3. Anda memiliki 3 nyawa.
         4. Total 60 detik akan disediakan.
         5. Timer dimulai setelah jawaban pertama dimasukkan """)
input("Are you ready ?? Tekan tombol apa saja untuk memulai ! ")
bermain = True
while(bermain):
    masukan = input('\n 1. Untuk memulai permainan \n 0. Keluar \n Silahkan masukkan pilihan anda : ')
    pilihan = masukan.strip().lower()
    if (pilihan in ('mulai', 'keluar')):
        if(pilihan == 'keluar'):
            bermain = False
        
    elif (pilihan in ('1', '0')):
        if(pilihan == '0'):
            bermain = False
        else :
            print('Silahkan masukkan nama anda : ')
            nama = input ()
            print('Helo!!, ' + nama)
            print('Silahkan jawab beberapa pertanyaan matematika dibawah ini dengan benar yaa, ' +nama)
        break
    else :
        print ('Maaf, saya tidak mengerti. Silahkan ulangi!!')
        break
    break

score = 0
level = 1
lives = 3
start = time.time()
finish_time = time.time() + 60 


while lives != 0 and time.time() < finish_time:
    
    if score != 0 and score % 5 == 0:
        level = level + 1
    print("LEVEL : ", level)
    no_of_operands = level + 1
    question_expression = generate_expression(no_of_operands)
    print(question_expression, end='')
    correct_answer = 0
    try:
        correct_answer = result(question_expression)
    except:
        print("OOPS ! ")
        continue
    answer = int(input(" = "))

    if evaluate(correct_answer, answer):
        print("Benar ! ", end='')
        score = score + 1
        print("Score = ", score, "Nyawa = ", lives)
    else:
        print("Salah ! ", end='')
        lives = lives - 1
        print("Score = ", score, "Nyawa = ", lives)
print("GAME OVER !!!")
print("Level Akhir = ", level, "Score = ", score)