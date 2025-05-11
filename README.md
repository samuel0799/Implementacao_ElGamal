# Implementacao da Criptografia ElGamal- Flask

Este projeto é uma implementação simples do algoritmo de criptografia ElGamal, com interface web feita em Flask. Permite cifrar e decifrar mensagens de texto, mostrando os pares cifrados prontos para copiar e colar.

## Funcionalidades

- **Cifrar mensagens:** Digite uma mensagem e obtenha os pares cifrados.
- **Decifrar mensagens:** Cole os pares cifrados e recupere a mensagem original.

## Como usar

### 1. Instale as dependências

```bash
pip install flask
```

### 2. Execute o servidor

```bash
python app.py
```

### 3. Acesse no navegador

Abra [http://localhost:5000/cifrar](http://localhost:5000/cifrar) para cifrar mensagens.

## Estrutura dos arquivos

- `app.py` — Código principal Flask.
- `elgamal.py` — Funções de criptografia e descriptografia.
- `templates/cifrar.html` — Página para cifrar mensagens.
- `templates/decifrar.html` — Página para decifrar mensagens.

## Exemplo de uso

1. **Cifrar:**  
   Digite sua mensagem e clique em "Cifrar".  
   Copie os pares cifrados exibidos no formato:  
   ```
   (a1,b1);(a2,b2);...
   ```

2. **Decifrar:**  
   Cole os pares cifrados no campo da página de decifrar e clique em "Decifrar" para ver a mensagem original.

## Observações

- Os parâmetros do ElGamal (p, g, x, y) estão definidos em `elgamal.py`.
- O sistema é apenas para fins didáticos e não deve ser usado em produção.

---

Desenvolvido para fins acadêmicos na UERN.
