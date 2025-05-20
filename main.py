# Import the necessary Flask components and os for environment variables
from flask import Flask, request, jsonify
import os # Import the os module to access environment variables

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/') that accepts GET requests
@app.route('/', methods=['GET'])
def generate_even_numbers():
    """
    Generates a fixed number of even numbers.
    The value of 'n' is now set directly within the program.
    Returns a JSON object containing the list of even numbers.
    """
    try:
        # Define 'n' directly within the program.
        # You can change this value to generate a different number of even numbers.
        n = 10 # Example: Generate the first 10 even numbers

        # Check if 'n' is a non-negative integer
        if n < 0:
             # If 'n' is negative, return an error message with a 400 status code
             # This check is still useful if 'n' is hardcoded to a negative value by mistake
             return jsonify({"error": "'n' must be a non-negative integer (set within the code)"}), 400

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

    except Exception as e:
        # Catch any unexpected errors
        # Return a generic internal server error message with a 500 status code
        return jsonify({"error": f"An internal error occurred: {str(e)}"}), 500

# This block is executed only when the script is run directly (not imported as a module)
if __name__ == '__main__':
    # Get the port from the environment variable 'PORT' provided by Railway, default to 5000 if not set
    # This is crucial for deployment on platforms like Railway
    port = int(os.environ.get('PORT', 5000))
    # Run the Flask application, binding to 0.0.0.0 to be accessible externally
    # Debug mode is set to False for production environments
    app.run(host='0.0.0.0', port=port, debug=False)
