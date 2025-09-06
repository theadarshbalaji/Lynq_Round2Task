# Import necessary libraries
import asyncio  # For asynchronous programming
from fastmcp import Client  # FastMCP client to connect to the weather tool

# List of known cities your bot can recognize
KNOWN_CITIES = ["Hyderabad", "Delhi", "Chennai", "Bangalore", "Mumbai", "Kolkata", "Pune"]

# Function to extract a city from user input
def extract_city(text):
    text = text.lower()  # Convert to lowercase for easy comparison
    for city in KNOWN_CITIES:
        if city.lower() in text:  # Check if city is mentioned in the input
            return city
    return None  # Return None if no known city is found

# Asynchronous main function to run the chatbot
async def main():
    # Create a FastMCP client and point it to the weather MCP server
    client = Client("http://127.0.0.1:8000/mcp")  # Server should already be running

    # Use the client in an async context
    async with client:
        print("You can ask about weather like: 'Is it raining in Hyderabad today?'")
        print("Type 'exit' to quit.\n")

        # Infinite loop to keep interacting with the user
        while True:
            user_input = input("You: ").strip()  # Get input from the user

            # If user wants to exit the chat
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")  # Friendly exit message
                break  # Exit the loop

            # Try to find a city in the user's question
            city = extract_city(user_input)
            if not city:
                print("AI: Sorry, I couldn't figure out which city you're asking about.")
                continue  # Skip this turn and wait for next input

            try:
                # Call the 'get_weather' tool from the MCP server with the detected city
                result = await client.call_tool("get_weather", {"city": city})

                # Display the result returned by the server
                print(f"AI: According to the weather API, {result.data}")

            except Exception as e:
                # Print any error that occurs during the API/tool call
                print("Error calling weather tool:", e)

# This runs the chatbot if the script is executed directly
if __name__ == "__main__":
    asyncio.run(main())  # Start the async event loop and run the main function
