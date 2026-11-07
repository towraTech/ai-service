import os
import uuid

import torch
from diffusers import AutoPipelineForText2Image


class ImageService:

    MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"

    def __init__(self):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        print(
            f"Loading image model on: {self.device}"
        )

        if self.device == "cuda":

            self.pipeline = AutoPipelineForText2Image.from_pretrained(
                self.MODEL_ID,
                torch_dtype=torch.float16,
                variant="fp16",
                use_safetensors=True,
            )

        else:

            self.pipeline = AutoPipelineForText2Image.from_pretrained(
                self.MODEL_ID,
                torch_dtype=torch.float32,
                use_safetensors=True,
            )

        self.pipeline = self.pipeline.to(
            self.device
        )

    def generate_image(
        self,
        prompt: str,
        output_dir: str = "outputs/images",
    ):

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        image_id = str(uuid.uuid4())

        filename = f"{image_id}.png"

        output_path = os.path.join(
            output_dir,
            filename
        )

        image = self.pipeline(
            prompt=prompt,
            num_inference_steps=30,
            guidance_scale=7.5,
            height=1024,
            width=1024,
        ).images[0]

        image.save(output_path)

        return {
            "success": True,
            "filename": filename,
            "path": output_path,
            "prompt": prompt,
        }