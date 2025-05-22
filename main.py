from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with form and output rendering
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Even Number Generator</title>
</head>
<body>
    <h2>Enter a number to generate even numbers</h2>
    <form method="POST">
        <input type="number" name="n" required>
        <button type="submit">Generate</button>
    </form>

    {% if even_numbers is not none %}
        <h3>Generated Even Numbers:</h3>
        <p>{{ even_numbers }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    even_numbers = None
    if request.method == 'POST':
        try:
            n = int(request.form['n'])
            even_numbers = [i for i in range(2, 2 * n + 1, 2)]
        except ValueError:
            even_numbers = "Invalid input. Please enter a valid number."

    return render_template_string(HTML_TEMPLATE, even_numbers=even_numbers)

if __name__ == '__main__':
    app.run(debug=True)
