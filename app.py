import random
import json
from flask import Flask, request, render_template, jsonify
from logic import get_next_state

app = Flask(__name__)

n = 20
m = 30
stored_grid = [[0 for _ in range(m)] for _ in range(n)]

@app.route('/', methods=['GET', 'POST'])
def index():
    global stored_grid

    if request.method == 'POST':
        action = request.form.get('action')
        print(f"Action received: {action}")

        if action == 'random':
            stored_grid = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
        
        elif action == 'reset':
            stored_grid = [[0 for _ in range(m)] for _ in range(n)]

        return render_template('index.html', grid=stored_grid, n=n, m=m)
    
    elif request.method == 'GET':
        return render_template('index.html', grid=stored_grid, n=n, m=m)

@app.route('/run', methods=['POST'])
def run():
    global stored_grid
    print("Processing current state after run")

    data = request.get_data(as_text=True)
    json_data = json.loads(data)
    grid = json_data.get('grid')
    stored_grid = grid

    return jsonify(grid=stored_grid)

@app.route('/next_state', methods=['POST'])
def next_state():
    global stored_grid
    print("Processing next state")
    next_grid = get_next_state(stored_grid)
    stored_grid = next_grid
    return jsonify(grid=stored_grid)

if __name__ == '__main__':
    app.run(debug=True)
