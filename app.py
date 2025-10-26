from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Configurações de segurança
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Arquivo para salvar a descrição
DESCRIPTION_FILE = 'description.json'

def load_description():
    """Carrega a descrição salva ou retorna uma padrão"""
    if os.path.exists(DESCRIPTION_FILE):
        try:
            with open(DESCRIPTION_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('description', 'Desenvolvedor apaixonado por tecnologia e inovação.')
        except:
            pass
    return 'Desenvolvedor apaixonado por tecnologia e inovação.'

def save_description(description):
    """Salva a descrição no arquivo"""
    # Validação básica de entrada
    if len(description) > 1000:  # Limite de caracteres
        description = description[:1000]
    
    # Sanitização básica
    description = description.replace('<script>', '').replace('</script>', '')
    
    with open(DESCRIPTION_FILE, 'w', encoding='utf-8') as f:
        json.dump({'description': description}, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    description = load_description()
    creation_date = "Outubro de 2025"
    current_year = datetime.now().year
    return render_template('index.html', 
                         description=description, 
                         creation_date=creation_date,
                         current_year=current_year)

@app.route('/update_description', methods=['POST'])
def update_description():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'Dados inválidos'}), 400
        
        description = data.get('description', '')
        if not isinstance(description, str):
            return jsonify({'success': False, 'error': 'Descrição deve ser texto'}), 400
        
        save_description(description)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': 'Erro interno'}), 500

# Para Vercel
def handler(request):
    return app(request.environ, lambda *args: None)

if __name__ == '__main__':
    # Configurações para desenvolvimento local
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
