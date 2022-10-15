# Используя input() ввести предложение состоящее из двух слов.
# Создать 2 переменные и в каждую записать по 1 введённому слову используя методы строк.
# Создать новую переменную 3-мя разными способами форматирования (фактически
# 3 переменные), которая бы состояла из введённых слов в обратном порядке, первое слово должно состоять только из
# больших букв, а второе с первой заглавной буквы и остальных маленьких. В начале предложения должен быть
# восклицательный знак, а в конце вопросительный.
# Используя только атрибуты функции print() вывести первоначальную строку и получившиеся
# разными способами форматирования через разделитель "<<<>>>", вывод сделать в файл.

any_word_1 = input("Enter any sentence: ")

print("Your sentence : ", any_word_1)

f_variable = any_word_1.split()[0]
s_variable = any_word_1.split()[1]

n_file = open('finite.txt', 'w')

th_variable = ("! Your sentence: %(form_1)s, %(form_2)s " % {'form_1': s_variable.upper()[::-1], 'form_2': f_variable[::-1].capitalize()})

fourth_variable = ("! Your sentence: {}, {} ".format(s_variable.upper()[::-1], f_variable[::-1].capitalize()))

fifth_variable = f"! Your sentence: {s_variable.upper()[::-1]}, {f_variable[::-1].capitalize()} "

print(th_variable, fourth_variable, fifth_variable, sep='? \n', end='? \n')
print(any_word_1, th_variable, fourth_variable, fifth_variable, sep=' <<<>>> ', end='\n', file=n_file)

n_file.close()
