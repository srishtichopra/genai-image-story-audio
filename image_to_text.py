from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def generate_caption(image_path):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    raw_image = Image.open(image_path).convert("RGB")
    inputs = processor(raw_image, return_tensors="pt")

    output = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

if __name__ == "__main__":
    test_caption = generate_caption("image.png")
    print("Generated caption:", test_caption)