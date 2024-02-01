import requests
from bs4 import BeautifulSoup
import pyfiglet

def print_banner():
    banner_text = pyfiglet.figlet_format("By Lucas R.", font="slant")
    print(banner_text)
    print("Bem vindo, esta e uma automocao do google hacking. Faca bom uso.")
    print("caso tenha alguma sugestao de melhora, entre em contato: @azxrs_")
    print("azx OSINT  v0.1")
    print("-" * 80)

def google_search(query, num_results=5):
    operators = [
        '"{}"',
        'site:{}',
        'intitle:{}',
        'inurl:{}',
        'intext:{}',
        'filetype:{}',
        'ext:{}',
        'cache:{}',
        '-{}',
    ]
      
    print_banner()
    
    for operator in operators:
        formatted_query = operator.format(query)
        url = f"https://www.google.com/search?q={formatted_query}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', class_='tF2Cxc')[:num_results]

            print(f"\nResults for: {formatted_query}\n")
            for i, result in enumerate(results, 1):
                link = result.find('a')['href']
                print(f"{i}. {link}")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao realizar sua pesquisa, tente novamente: {e}")

def main():
    while True:
        user_query = input("Digite o que deseja buscar: ")
        num_results = int(input("Quantos resultados vc quer? (recomendado:  5): ") or 5)
        
        google_search(user_query, num_results)

        new_query = input("iai, ta afim de mais alguma  consulta? :)  (s/n): ").lower()
        if new_query != 's':
            break

if __name__ == "__main__":
    main()
