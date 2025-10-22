from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

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
    with open(DESCRIPTION_FILE, 'w', encoding='utf-8') as f:
        json.dump({'description': description}, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    description = load_description()
    return render_template('index.html', description=description)

@app.route('/update_description', methods=['POST'])
def update_description():
    data = request.get_json()
    description = data.get('description', '')
    save_description(description)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
