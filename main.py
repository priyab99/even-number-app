from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Enter a number to generate even numbers</h2>
        <form action="/generate" method="get">
            Enter a number: <input type="text" name="n">
            <input type="submit" value="Generate">
        </form>
    '''

@app.route('/generate')
def generate_even():
    try:
        n = int(request.args.get('n', 0))
        evens = [str(i * 2) for i in range(n)]
        return f"<h3>First {n} even numbers:</h3><p>{', '.join(evens)}</p>"
    except ValueError:
        return "Please enter a valid integer."

if __name__ == '__main__':
    app.run()
