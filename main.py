# app.py

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with form and output rendering
# Added meta viewport for responsiveness and Tailwind CSS for basic styling
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Even Number Generator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom font for a clean look */
        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
</head>
<body class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen flex items-center justify-center p-4">
    <div class="bg-white p-8 rounded-xl shadow-2xl w-full max-w-md text-center border border-gray-200">
        <h2 class="text-4xl font-extrabold text-gray-800 mb-6">Even Number Generator</h2>
        <p class="text-gray-600 mb-8">Enter a positive integer 'n' to generate the first 'n' even numbers.</p>

        <form method="POST" class="space-y-6">
            <div class="relative">
                <input
                    type="number"
                    id="number_n"
                    name="n"
                    placeholder=" "
                    required
                    min="1"
                    class="block w-full px-4 py-3 text-lg text-gray-900 bg-gray-50 border border-gray-300 rounded-lg appearance-none focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent peer"
                />
                <label
                    for="number_n"
                    class="absolute text-gray-500 text-lg duration-300 transform -translate-y-1/2 scale-75 top-1/2 left-4 z-10 origin-[0] peer-focus:scale-75 peer-focus:-translate-y-6 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:top-1/2 peer-focus:left-4 peer-focus:z-0"
                >
                    Enter n
                </label>
            </div>
            <button
                type="submit"
                class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75"
            >
                Generate
            </button>
        </form>

        {% if even_numbers is not none %}
            <div class="mt-8">
                {% if even_numbers is string %} {# Check if it's an error message #}
                    <h3 class="text-2xl font-bold text-red-600 mb-4">Error:</h3>
                    <p class="text-red-500 text-lg">{{ even_numbers }}</p>
                {% else %}
                    <h3 class="text-2xl font-bold text-gray-800 mb-4">Generated Even Numbers:</h3>
                    <div class="bg-gray-50 p-6 rounded-lg border border-gray-200">
                        <ul class="list-none p-0 m-0 grid grid-cols-2 sm:grid-cols-3 gap-3 text-lg text-gray-700">
                            {% for num in even_numbers %}
                                <li class="bg-blue-100 text-blue-800 px-4 py-2 rounded-md font-semibold shadow-sm">{{ num }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                {% endif %}
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    even_numbers = None
    if request.method == 'POST':
        try:
            n_str = request.form.get('n') # Use .get() for safer access
            if not n_str:
                even_numbers = "Please enter a number."
            else:
                n = int(n_str)
                if n <= 0:
                    even_numbers = "Please enter a positive integer for 'n'."
                else:
                    # Generate 'n' even numbers, starting from 0 (or 2 if you prefer)
                    # The original code generates [2, 4, ..., 2*n]
                    # This generates [0, 2, ..., 2*(n-1)]
                    # If you want [2, 4, ..., 2*n], use: even_numbers = [2 * i for i in range(1, n + 1)]
                    even_numbers = [2 * i for i in range(n)]
        except ValueError:
            even_numbers = "Invalid input. Please enter a whole number."
        except Exception as e:
            even_numbers = f"An unexpected error occurred: {str(e)}"

    return render_template_string(HTML_TEMPLATE, even_numbers=even_numbers)

if __name__ == '__main__':
    # This block is for local development only.
    # In production (Railway), Gunicorn will run the app.
    app.run(debug=True)
