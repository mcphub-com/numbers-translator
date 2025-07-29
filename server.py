import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/orthosie/api/numbers-translator'

mcp = FastMCP('numbers-translator')

@mcp.tool()
def numbers_translator(text: Annotated[Union[str, None], Field(description='Numerical value of the number')] = None) -> dict: 
    '''Numbers Translator'''
    url = 'https://numbers-spell.p.rapidapi.com/numbers'
    headers = {'x-rapidapi-host': 'numbers-spell.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'text': text,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
