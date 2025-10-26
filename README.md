# Portfolio Terroso

Um portfólio moderno e elegante com tema terroso, desenvolvido em Flask.

## 🚀 Deploy no Vercel

### Pré-requisitos
- Conta no [Vercel](https://vercel.com)
- Conta no [GitHub](https://github.com)

### Passos para Deploy

1. **Fazer upload do projeto para o GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/portfolio-terroso.git
   git push -u origin main
   ```

2. **Conectar ao Vercel:**
   - Acesse [vercel.com](https://vercel.com)
   - Clique em "New Project"
   - Importe o repositório do GitHub
   - Configure as variáveis de ambiente (opcional)

3. **Deploy automático:**
   - O Vercel detectará automaticamente que é um projeto Python/Flask
   - O deploy será feito automaticamente

### 🔒 Segurança

O projeto inclui várias medidas de segurança:

- ✅ Validação de entrada de dados
- ✅ Sanitização básica contra XSS
- ✅ Limite de caracteres na descrição
- ✅ Tratamento de erros
- ✅ Configuração de produção
- ✅ Arquivo .gitignore para proteger dados sensíveis

### 📁 Estrutura do Projeto

```
portfolio-terroso/
├── app.py                 # Aplicação Flask principal
├── vercel.json           # Configuração do Vercel
├── requirements.txt      # Dependências Python
├── .gitignore           # Arquivos ignorados pelo Git
├── description.json      # Dados da descrição (criado automaticamente)
├── templates/
│   └── index.html       # Template principal
└── static/
    └── styles.css       # Estilos CSS
```

### 🛠️ Desenvolvimento Local

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar localmente
python app.py
```

### 🌐 Acesso

Após o deploy, seu portfólio estará disponível em:
`https://SEU_PROJETO.vercel.app`

### 📝 Funcionalidades

- ✅ Design responsivo
- ✅ Edição de descrição em tempo real
- ✅ Animações CSS
- ✅ Seção de habilidades
- ✅ Links de redes sociais
- ✅ Rodapé com créditos
- ✅ Tema terroso elegante

### 🔧 Personalização

Para personalizar o portfólio:

1. **Alterar informações pessoais:** Edite o template `templates/index.html`
2. **Modificar cores:** Ajuste as variáveis CSS em `static/styles.css`
3. **Adicionar habilidades:** Modifique a seção de skills no HTML
4. **Atualizar links sociais:** Altere os links na seção social

### 📞 Suporte

Se tiver problemas com o deploy, verifique:
- Se todas as dependências estão no `requirements.txt`
- Se o arquivo `vercel.json` está correto
- Se não há erros nos logs do Vercel