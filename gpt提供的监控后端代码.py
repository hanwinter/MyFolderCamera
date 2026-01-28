from flask import Flask, request, jsonify, render_template
import sqlite3
from io import BytesIO
from PIL import Image
import base64

app = Flask(__name__)

# 创建数据库并初始化表
def init_db():
    conn = sqlite3.connect('camera.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS frames (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image BLOB
        )
    ''')
    conn.commit()
    conn.close()
@app.route('/')
def index():
    return render_template('index.html')

# 保存图像到数据库
@app.route('/save-frame', methods=['POST'])
def save_frame():
    data = request.get_json()
    image_data = data.get('image')

    if not image_data:
        return jsonify({'error': '没有接收到图像数据'}), 400

    # 去掉前缀部分
    image_data = image_data.split(',')[1]
    image_bytes = base64.b64decode(image_data)

    # 将图像保存到数据库
    conn = sqlite3.connect('camera.db')
    c = conn.cursor()
    c.execute('INSERT INTO frames (image) VALUES (?)', (image_bytes,))
    conn.commit()
    conn.close()

    return jsonify({'message': '图像保存成功'}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
