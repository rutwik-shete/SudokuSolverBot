
from promptflow import tool
from model_files.model import SudokuModel
import PIL.Image as Image
import numpy as np
import io
import requests


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input_image) -> str:
    
    # response_image = requests.get(input_image)
    # mage_bytes = io.BytesIO(response_image.content)

    image_byteIO = io.BytesIO(input_image)

    captioning_model = SudokuModel()

    image = Image.open(image_byteIO).convert("RGB")
    caption = captioning_model(image)


    return caption

