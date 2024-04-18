from flask import Flask, render_template, request, jsonify
import yaml
import uuid
import pyperclip  # для копирования в буфер обмена

app = Flask(__name__)

# Генерация GUID
def generate_guid():
    return str(uuid.uuid4()).replace('-', '')[:34]

# Основной маршрут для отображения формы и обработки данных
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        team = request.form['team']
        project = request.form['project']
        environment = request.form['environment']
        patterns = request.form['pattern'].split('/n')
        description = request.form['description']
        
        # Генерация GUID
        guid = generate_guid()
        
        # Создание YAML
        yaml_data = {
            f"{team}-{project}-{environment}-{guid}": [
                  pattern,
                  f"{pattern}-????.??.??"
            
            ]
        }
        
        # Добавление описания в комментарий
        yaml_str = yaml.dump(yaml_data)
        yaml_str = yaml_str.replace("#", f"# {description}", 1)  # добавляем описание

        # Копирование в буфер обмена
        pyperclip.copy(yaml_str)

        return jsonify({'yaml_str': yaml_str})  # Отправляем YAML как JSON

    return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=True)