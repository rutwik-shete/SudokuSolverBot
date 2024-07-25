import torch
import torch.nn as nn
from transformers import AutoProcessor, Pix2StructForConditionalGeneration
# from diffusers import StableDiffusionUpscalePipeline

processor = AutoProcessor.from_pretrained("ybelkada/pix2struct-base")
captioning_model = Pix2StructForConditionalGeneration.from_pretrained("ybelkada/pix2struct-base")
ckpt = torch.load("./pretrained_models/model.pth.tar-150.00.ckpt")
captioning_model.load_state_dict(ckpt["state_dict"])

# model_id = "stabilityai/stable-diffusion-x4-upscaler"
# upscaling_model = StableDiffusionUpscalePipeline.from_pretrained(model_id,revision="fp16", torch_dtype=torch.float32)

processor.save_pretrained("./pretrained_models/auto_processor")
captioning_model.save_pretrained("./pretrained_models/captioning_model")
# upscaling_model.save_pretrained("./app/upscaling_model")