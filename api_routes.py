from flask import Blueprint, request, jsonify, session
import sqlite3

api_bp = Blueprint('api', __name__, url_prefix="/api")

def get_db():
    return sqlite3.connect("data.db")

@api_bp.route("/insert", methods=["POST"])
def insert_temperature():
    data = request.get_json()
    temp = data.get("temperature")
    if temp is None:
        return jsonify({"error": "Temperature value is required"}), 400
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO Data (temperature) VALUES (?)", (temp,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Inserted"}), 201

@api_bp.route("/last", methods=["GET"])
def get_last():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM Data ORDER BY id DESC LIMIT 1")
    row = c.fetchone()
    conn.close()
    if row is None:
        return jsonify({"error": "No data available"}), 404
    return jsonify({"id": row[0], "temperature": row[1], "timestamp": row[2]})

@api_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM Data WHERE id = ?", (id,))
    row = c.fetchone()
    conn.close()
    return jsonify(row)

@api_bp.route("/delete_oldest", methods=["DELETE"])
def delete_oldest():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    conn = get_db()
    c = conn.cursor()
    c.execute("DELETE FROM Data WHERE id = (SELECT id FROM Data ORDER BY id LIMIT 1)")
    conn.commit()
    conn.close()
    return jsonify({"message": "Oldest deleted"})

@api_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_by_id(id):
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    conn = get_db()
    c = conn.cursor()
    c.execute("DELETE FROM Data WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Deleted ID {id}"})

# BONUS
@api_bp.route("/all", methods=["GET"])
def get_all():
    sort = request.args.get("sort", "asc")
    order = "ASC" if sort == "asc" else "DESC"
    conn = get_db()
    c = conn.cursor()
    c.execute(f"SELECT * FROM Data ORDER BY id {order}")
    rows = c.fetchall()
    conn.close()
    data = [{"id": row[0], "temperature": row[1], "timestamp": row[2]} for row in rows]
    return jsonify(data)
