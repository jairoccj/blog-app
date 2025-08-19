import os
ARQUIVO_CSV = "app/posts.csv"

def inicializar_csv() -> None:
    if not os.path.exists(ARQUIVO_CSV):
        arq = open(ARQUIVO_CSV, "w")
        arq.write("title, content\n")
        arq.close()

def ler_csv() -> list:
    posts = []
    if os.path.exists(ARQUIVO_CSV):
        arq = open(ARQUIVO_CSV, 'r')
        linhas = arq.read().splitlines()
        arq.close()

        for i in range(1, len(linhas)):
            partes = linhas[i].split(',')
            title = partes[0]
            content = ','.join(partes[1:])
            posts.append({'title': title, 'content': content})
        
        return posts
    
def reescrever_csv(posts: list) -> None:
    arq = open(ARQUIVO_CSV, 'w')
    linhas = ['title,content']

    for post in posts:
        linhas.append(f"{post['title']}, {post['content']}")

    conteudo = '\n'.join(linhas) + '\n'
    arq.write(conteudo)
    arq.close()

def escrever_csv(title: str, content: str) -> None:
    arq = open(ARQUIVO_CSV, 'a')
    arq.write(f"{title},{content}\n")
    arq.close()