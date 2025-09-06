from fastmcp import FastMCP, Client  # Import FastMCP for creating the server
import requests  # Used to make HTTP requests to OpenWeather API

# Create an instance of FastMCP server and give it a name
mcp = FastMCP(name="WeatherServer")

# Your OpenWeather API key (replace with your actual key if needed)
API_KEY = "f7a5a107de9ea066797fd94dbcd4b042"

# Define and register a tool using the @mcp.tool() decorator
# This function can now be called remotely by MCP clients
@mcp.tool()
def get_weather(city: str) -> str:
    # Build the OpenWeather API URL with the provided city and API key
    url = (f"http://api.openweathermap.org/data/2.5/weather"
           f"?q={city}&appid={API_KEY}&units=metric")
    
    # Send a GET request to the OpenWeather API
    response = requests.get(url)

    # If the request failed (bad city name, bad key, etc.), return an error message
    if response.status_code != 200:
        return f"Could not fetch weather for {city}. (Error {response.status_code})"

    # Parse the JSON response
    data = response.json()

    # Extract useful weather information
    weather_desc = data['weather'][0]['description']  # e.g., 'light rain'
    temp = data['main']['temp']  # Temperature in Celsius
    
    # Return a nicely formatted weather report
    return f"According to the weather API, it's {weather_desc}, {temp}°C in {city}."

# Start the MCP server when this file is run directly
if __name__ == "__main__":
    # Start the server on localhost, port 8000, at path "/mcp"
    mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
