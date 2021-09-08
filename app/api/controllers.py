from flask import Blueprint, jsonify

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/status')
def api_status():
    return jsonify(status='ok')