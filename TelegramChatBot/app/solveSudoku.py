import base64
import os
from dotenv import load_dotenv
import aiohttp

load_dotenv("./keys.env")

PROMPTFLOW_API_LINK = os.environ.get('PROMPTFLOW_API')
print("This is link key :",PROMPTFLOW_API_LINK)
async def solveSudoku(IMAGE_PATH):

    # Read image data and encode as base64
    with open(IMAGE_PATH, "rb") as image_file:
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")

    print("Got the image")
    # Prepare the request payload
    payload = {
        "query_image": image_base64
    }

    # Send the request
    # response = await asyncio.gather(requests.post(PROMPTFLOW_API_LINK, json=payload))
    async with aiohttp.ClientSession() as session:
        async with session.post(PROMPTFLOW_API_LINK,json=payload) as resp:
            if resp.status == 200:
                # solved_sudoku_output = await resp.json()['solved_sudoku_output']
                # return json.loads(solved_sudoku_output)
                print("Got Data")
                return await resp.json()
            else:
                print("Got Error")
                print("Error:", resp.text())

    # # Handle the response
    # if response.status_code == 200:
    #     solved_sudoku_output = response.json()['solved_sudoku_output']
    #     return json.loads(solved_sudoku_output)
    # else:
    #     print("Error:", response.text)