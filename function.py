import json
import os
import openai
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://neyahopenai.openai.azure.com/",
    api_version="2023-06-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
def get_stock_price(symbol):
    """Get the current stock price for given symbol"""
    stock_info = {
        "symbol": symbol,
        "price": "1000"
    }
    return json.dumps(stock_info)


functions = [
    {
        "name": "get_stock_price",
        "description": "Get the current stock price for the given symbol",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The symbol, e.g. AAPL",
                }
            },
            "required": ["symbol"],
        },
    }
]
response = client.chat.completions.create(
    model= "text-demo",
    messages=[{"role":"user","content": "Hello World"}],
    function_call="auto",
    functions= functions
)
response_message = response.choices[0].message
if response_message.function_call:
    functions_args=json.loads(response_message.function_call.arguments)
print(get_stock_price(functions_args.get("symbol")))





