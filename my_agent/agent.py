import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

def cal(x: int, opt: str, y: int, ) -> dict:
    """Performs a simple calculation based on the provided operation.

    Args:
        x (int): The first integer.
        y (int): The second integer.
        opt (str): The operation to perform ("add", "subtract", "multiply", "divide").

    Returns:
        dict: status and result.
    """
    if opt == "add":
        result = x + y
    elif opt == "subtract":
        result = x - y
    elif opt == "multiply":
        result = x * y
    elif opt == "divide":
        if y == 0:
            return {"status": "error", "error_message": "Division by zero is not allowed."}
        result = x / y
    else:
        return {"status": "error", "error_message": f"Unsupported operation '{opt}'."}
    return {"status": "success", "result": result}

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time, weather in a city, and perform simple calculations."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city, and you can also perform simple calculations."
    ),
    tools=[get_weather, get_current_time, cal],
)