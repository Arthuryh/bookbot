import sys
from stats import count_words, count_characters, sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Como usar: python3 main.py <caminho absoluto arquivo>")
        sys.exit(1)
    else:
        print("================= BOOKBOT =================")
        print(f"Analisando o livro encontrado em {sys.argv[1]}...")
        num_words = count_words(get_book_text(sys.argv[1]))
        num_charac = count_characters(get_book_text(sys.argv[1]))
        sorted_list = sort_list(num_charac)
        print("----------- Contagem de Palavras ----------")
        print(f"Encontrado um total de {num_words} palavras")
        print("---------- Contagem de Caracteres --------")
        for i in sorted_list:
            if i["name"].isalpha() == True:
                print(f"{i["name"]}: {i["num"]}")
            else:
                pass
        print("================== FIM ===================")
main()