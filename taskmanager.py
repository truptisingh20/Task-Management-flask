from flask import Flask, request, render_template_string

app = Flask(__name__)

# List to store tasks
tasks = []

@app.route("/", methods=["GET", "POST"])
def task_manager():
    if request.method == "POST":
        task_title = request.form["task_title"]
        task_description = request.form["task_description"]
        
        # Add the task to the list
        tasks.append({"title": task_title, "description": task_description})
    
    # Render the page with tasks
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Task Management System</title>
    </head>
    <body>
        <h1>Task Management System</h1>
        
        <form method="POST" action="/">
            <label for="task_title">Task Title:</label>
            <input type="text" id="task_title" name="task_title" required>
            <br>
            
            <label for="task_description">Task Description:</label>
            <textarea id="task_description" name="task_description" rows="4" required></textarea>
            <br>
            
            <input type="submit" value="Add Task">
        </form>
        
        <h2>Tasks List</h2>
        {% for task in tasks %}
            <div>
                <h3>{{ task.title }}</h3>
                <p>{{ task.description }}</p>
            </div>
        {% endfor %}
    </body>
    </html>
    ''', tasks=tasks)

if __name__ == "_main_":
    app.run(debug=True)