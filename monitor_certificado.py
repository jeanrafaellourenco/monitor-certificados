import requests
import json
import time

def fetch_unique_urls(domain, output_file, retries=5, delay=10):
    url = f"https://crt.sh/json?q={domain}&exclude=expired&group=none"

    for attempt in range(retries):
        try:
            # Fazendo a requisição à API do crt.sh
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            
            # Parse do JSON retornado
            data = response.json()

            # Extraindo os nomes únicos dos certificados
            unique_urls = set()
            for entry in data:
                if 'name_value' in entry:
                    subdomains = entry['name_value'].split("\n")
                    unique_urls.update(subdomains)

            # Sobrescrevendo o arquivo de saída com as URLs únicas
            with open(output_file, "w") as file:
                for url in sorted(unique_urls):
                    file.write(f"{url}\n")

            print(f"URLs salvas em: {output_file}")
            return  # Finaliza após sucesso
        except requests.exceptions.RequestException as e:
            print(f"Tentativa {attempt + 1}/{retries} falhou: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                print(f"Erro persistente ao acessar {url}. Verifique o serviço.")
        except json.JSONDecodeError:
            print("Erro ao decodificar a resposta JSON.")
            return

if __name__ == "__main__":
    domain = input("Digite o domínio a ser monitorado: ")
    output_file = f"{domain}_unique_urls.txt"
    fetch_unique_urls(domain, output_file)
