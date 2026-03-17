# cree una funcion que acepte un string con palabra separadas por un guion #
# y que retorne un string igual pero ordenado alfabeticamente

text = "python-variable-computadora-monitor"

def split_first(text):
    return text.split("-") 

def sort_second(words):   
    for i in range(len(words) - 1):
        for j in range(len(words) - 1 - i):
            if ord(words[j][0]) > ord(words[j + 1][0]):   
                words[j], words[j + 1] = words[j + 1], words[j]   
    return words  

def join_third(words):
    return "-".join(words)  

def main(text):
    words = split_first(text)   
    sorted_words = sort_second(words)   
    final_text = join_third(sorted_words)   
    print(final_text)  


main(text)
