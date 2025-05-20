# Import the necessary Flask components
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/') that accepts GET requests
@app.route('/', methods=['GET'])
def generate_even_numbers():
    """
    Generates a specified number of even numbers based on the 'n' query parameter.
    Returns a JSON object containing the list of even numbers.
    """
    try:
        # Get the value of the 'n' query parameter from the request URL
        # For example, if the URL is /?n=10, request.args.get('n') will be '10'
        n_str = request.args.get('n')

        # Check if 'n' parameter is provided
        if not n_str:
            # If 'n' is missing, return an error message with a 400 status code (Bad Request)
            return jsonify({"error": "Please provide the 'n' parameter in the URL (e.g., /?n=10)"}), 400

        # Convert the 'n' parameter string to an integer
        n = int(n_str)

        # Check if 'n' is a non-negative integer
        if n < 0:
             # If 'n' is negative, return an error message with a 400 status code
             return jsonify({"error": "'n' must be a non-negative integer"}), 400

        # Initialize an empty list to store the even numbers
        even_numbers = []
        # Initialize a counter for even numbers found
        count = 0
        # Start checking numbers from 0
        num = 0

        # Loop until we have generated 'n' even numbers
        while count < n:
            # Check if the current number is even (divisible by 2 with no remainder)
            if num % 2 == 0:
                # If it's even, add it to our list
                even_numbers.append(num)
                # Increment the count of even numbers found
                count += 1
            # Move to the next number
            num += 1

        # Return the list of generated even numbers as a JSON response
        return jsonify({"even_numbers": even_numbers})

    except ValueError:
        # If the 'n' parameter cannot be converted to an integer, catch the ValueError
        # Return an error message indicating invalid input with a 400 status code
        return jsonify({"error": "Invalid input for 'n'. Please provide an integer."}), 400
    except Exception as e:
        # Catch any other unexpected errors
        # Return a generic internal server error message with a 500 status code
        return jsonify({"error": f"An internal error occurred: {str(e)}"}), 500

# This block is executed only when the script is run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application
    # debug=True allows for automatic reloading on code changes and provides a debugger
    # In a production environment, you would typically use a production-ready WSGI server
    app.run(debug=True)
