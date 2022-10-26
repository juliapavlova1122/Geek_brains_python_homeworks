# 3. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв".

input_text = input("Введите слова через пробел: ")

def words_delete(input_text):
    if not input_text:
        return ""
    input_text = list(filter(lambda x: 'абв' not in x, input_text.split()))
    return " ".join(input_text)

input_text = words_delete(input_text)
print(f'Слова, не содержащие "абв": ', input_text)

exit()
input_str = input()
text1 = "абв"
input_list = input_str.split() # разбили по словам
result_list = []
for word in input_list:
    if text1 not in word:
        result_list.append(word)
print(" ".join(result_list))


