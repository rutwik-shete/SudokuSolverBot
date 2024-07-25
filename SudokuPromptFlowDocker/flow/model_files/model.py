import torch
import torch.nn as nn
from transformers import AutoProcessor, Pix2StructForConditionalGeneration
from diffusers import StableDiffusionUpscalePipeline
import PIL.Image as Image


# Define and train your PyTorch model
class SudokuModel(nn.Module):
    def __init__(self):
        super(SudokuModel, self).__init__()
        self.device = torch.device("cpu")
        self.processor = AutoProcessor.from_pretrained("./pretrained_models/auto_processor")
        self.captioning_model = Pix2StructForConditionalGeneration.from_pretrained("./pretrained_models/captioning_model")
        # self.ckpt = torch.load("./model.pth.tar-150.00.ckpt")
        # self.captioning_model.load_state_dict(self.ckpt["state_dict"])

        self.captioning_model.to(self.device)

        # model_id = "./upscaling_model"
        # self.upscaling_model = StableDiffusionUpscalePipeline.from_pretrained(model_id,revision="fp16", torch_dtype=torch.float32)

        # self.upscaling_model = self.upscaling_model.to(self.device)

    def forward(self, x):
        # Define the forward pass

        # low_res_img = x.resize((128, 128))
        # prompt = "A Sudoku Puzzle With High Contrast In Digits"

        # upscaled_image = self.upscaling_model(prompt=prompt, image=low_res_img).images[0]
       
        print("Starting")
        encoding = self.processor(images=x, return_tensors="pt", add_special_tockens=True, max_patches=1024)
        encoding = {k:v.squeeze() for k,v in encoding.items()}

        print("Done With Processor")
        flattened_patches = encoding["flattened_patches"].to(self.device)
        flattened_patches = torch.stack([flattened_patches])
        attention_mask = encoding["attention_mask"].to(self.device)
        attention_mask = torch.stack([attention_mask])

        print("Done With Image Flattening")
        predictions = self.captioning_model.generate(flattened_patches=flattened_patches,
                                        attention_mask=attention_mask,
                                        max_length=100)
        
        print("Done With Generating Caption")
        generated_caption = self.processor.batch_decode(predictions, skip_special_tokens=True)
        
        print("Predictions : ", generated_caption)

        return ''.join(generated_caption)