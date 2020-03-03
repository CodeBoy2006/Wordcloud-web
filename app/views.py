import os

from app import app
from flask import request, Response, jsonify, make_response, abort, url_for
from app.core.Main import create_image_by_url,create_image_by_text

# @app.route('/')
@app.route('/app/wc_api',methods=['POST'])
def index():
    data = request.json  # 获取 JSON 数据
    print(data)
    text = data.get('text')     #  以字典形式获取参数
    split_mode = data.get('split_mode')
    wordscount = data.get('wordscount')
    result = create_image_by_text(text, split_mode, wordscount)
    return jsonify(result)


basedir = os.path.abspath(os.path.dirname(__file__))
@app.route('/image/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir, app.config['IMAGE_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            abort(404)
            pass
        else:
            if os.path.exists(os.path.join(file_dir, '%s' % filename)):
                image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
                response = make_response(image_data)
                response.headers['Content-Type'] = 'image/png'
                return response
            else:
                abort(404)
                pass
    else:
        abort(404)
        pass

