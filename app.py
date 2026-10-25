from flask import Flask, jsonify

app=Flask(__name__)

students = [
    {"id": 1, "name": "Asha Rao", "course": "Electronics", "year": 3},
    {"id": 2, "name": "Rahul Kumar", "course": "Computer Science", "year": 2},
    {"id": 3, "name": "Meera Nair", "course": "Information Science", "year": 4}
]

@app.get("/")
def home():
    return jsonify({
        "message": "Student Information API",
        "endpoints": ["/health", "/students", "/students/<id>"]
    }), 200

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/students")
def get_students():
    return jsonify({
        "count": len(students),
        "students": students
    }), 200

@app.get("/students/<int:student_id>")
def get_student(student_id):
    if student_id <= 0:
        return jsonify({
            "error": "Student ID must be a positive integer"
        }), 400
    
    for student in students:
        if student["id"] == student_id:
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)