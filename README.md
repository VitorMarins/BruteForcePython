# Demonstração de Ataque de Força Bruta

Este projeto é uma **demonstração educacional** de como um ataque de força bruta pode ser implementado contra um formulário de login. Ele foi criado exclusivamente para fins> fins acadêmicos, para mostrar aos alunos como esse tipo de ataque funciona e destacar a importância de boas práticas de segurança.

> **Aviso Legal**: Este código **não deve ser usado em sistemas reais sem permissão explícita do proprietário**. Ataques de força bruta em sites ou sistemas sem autorização são ilegais e antiéticos.

## Descrição

O script `brute_force.py` simula um ataque de força bruta enviando requisições POST a um formulário de login com diferentes combinações de senhas. Ele é projetado para ser simples e educativo, não refletindo todas as complexidades ou defesas de sistemas reais.

## Pré-requisitos

- Python 3.x
- Biblioteca `requests` (instale com `pip install requests`)
- Opcional: Flask (para criar um site de teste local - `pip install flask`)

## Como Usar

1. **Configurar um ambiente de teste**:
   - Use o script `test_server.py` para criar um servidor local de teste:
     ```bash
     python test_server.py
     ```
   - Isso inicia um servidor na URL `http://127.0.0.1:5000/login` com um usuário `admin` e senha `secret123`.

2. **Executar o ataque**:
   - Abra o arquivo `brute_force.py` e ajuste a `target_url` para a URL do seu servidor de teste (ex.: `http://127.0.0.1:5000/login`).
   - Edite a lista de senhas (`passwords`) para incluir as senhas que deseja testar.
   - Execute o script:
     ```bash
     python brute_force.py
     ```

3. **Observar os resultados**:
   - O script tentará cada senha da lista e exibirá se a senha foi encontrada ou não.

## Estrutura do Projeto

- `brute_force.py`: Script principal que executa o ataque de força bruta.
- `test_server.py`: Script opcional para criar um servidor de teste local.

## Exemplo de Saída

` Iniciando ataque de força bruta...
Tentativa 1: Testando senha '123456'
Tentativa 2: Testando senha 'password'
Tentativa 3: Testando senha 'secret123'
[+] Senha encontrada: secret123
[+] Tentativas necessárias: 3 `


## Limitações

- Este é um exemplo simplificado. Sites reais possuem defesas como:
  - CAPTCHAs
  - Bloqueio de IP após várias tentativas
  - Autenticação em dois fatores
- A lógica de sucesso/falha depende da resposta do servidor e pode precisar de ajustes.

## Objetivo Educacional

- Demonstrar como ataques de força bruta funcionam.
- Ensinar a importância de:
  - Senhas fortes e únicas.
  - Limitação de tentativas de login.
  - Monitoramento de atividades suspeitas.

## Ética e Responsabilidade

- **Não use este código em sistemas reais sem permissão.**
- Respeite as leis locais e as políticas de uso de qualquer sistema.
- Este projeto é apenas para aprendizado e não deve ser modificado para fins maliciosos.

## Contribuições

Sinta-se à vontade para sugerir melhorias ou ajustes para tornar o projeto mais educativo! Crie um *pull request* ou abra uma *issue*.
