from flask import Blueprint, jsonify
from .services import get_all_songs

#mock routes to call all service logic
bp =Blueprint("main", __name__)

@bp.route("/songs")
def songs():
    return jsonify(get_all_songs)