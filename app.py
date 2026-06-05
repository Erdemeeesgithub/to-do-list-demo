from flask import Flask, request, jsonify, render_template, send_from_directory
from heap import MinHeap

app = Flask(__name__)
heap = MinHeap()

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

@app.route('/add', methods=['POST'])
def add_task():
    data = request.json
    task = {
        'name': data['name'],
        'priority': int(data['priority']),
        'deadline': data.get('deadline', '')
    }
    heap.push(task)
    return jsonify({'heap': heap.heap})

@app.route('/pop', methods=['POST'])
def pop_task():
    if not heap.heap:
        return jsonify({'error': 'no tasks'}), 400
    task = heap.pop()
    return jsonify({'task': task, 'heap': heap.heap})

if __name__ == '__main__':
    app.run(debug=True)