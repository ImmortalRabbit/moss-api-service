from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from utils import put_text_into_files, moss_create_report_rage, moss_parse_html
import json


app = Flask(__name__)
api = Api(app)
           
class MossAPI(Resource):
    def post(self):
        content = request.get_json(force=True)
        base_file_code = content['basefile']
        comparison_files_codes = content['comparison_files']
        put_text_into_files(base_file_code, comparison_files_codes)
        moss_create_report_rage(comparison_files_codes)
        
        return jsonify(moss_parse_html())

api.add_resource(MossAPI, '/')

if __name__ == '__main__':  
    app.run(debug=True)