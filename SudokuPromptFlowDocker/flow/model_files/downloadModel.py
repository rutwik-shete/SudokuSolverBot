import torch
import torch.nn as nn
from transformers import AutoProcessor, Pix2StructForConditionalGeneration
import gdown
# from diffusers import StableDiffusionUpscalePipeline

processor = AutoProcessor.from_pretrained("ybelkada/pix2struct-base")
captioning_model = Pix2StructForConditionalGeneration.from_pretrained("ybelkada/pix2struct-base")
model_url = "https://drive.google.com/file/d/10nzai77hBnWxnjlvLjlCc2SI8x0PXXL4/view?usp=share_link"
output = "./flow/pretrained_models/SudokuTextExtractorPix2Struct.ckpt"
gdown.download(model_url, output, quiet=False, fuzzy=True)

ckpt = torch.load("./flow/pretrained_models/SudokuTextExtractorPix2Struct.ckpt")
captioning_model.load_state_dict(ckpt["state_dict"])

# model_id = "stabilityai/stable-diffusion-x4-upscaler"
# upscaling_model = StableDiffusionUpscalePipeline.from_pretrained(model_id,revision="fp16", torch_dtype=torch.float32)

processor.save_pretrained("./flow/pretrained_models/auto_processor")
captioning_model.save_pretrained("./flow/pretrained_models/captioning_model")
# upscaling_model.save_pretrained("./app/upscaling_model")