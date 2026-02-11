import os
from PIL import Image, ImageDraw, ImageFont

IMAGES_DIR = "assets/images"
OUTPUT_DIR = "output"
THUMBNAIL_PATH = os.path.join(OUTPUT_DIR, "thumbnail.jpg")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_thumbnail(topic: str):
    # Pick first available image
    images = [
        os.path.join(IMAGES_DIR, img)
        for img in os.listdir(IMAGES_DIR)
        if img.endswith(".jpg")
    ]

    if not images:
        raise ValueError("No images found to create thumbnail")

    base_image = Image.open(images[0]).convert("RGB")
    base_image = base_image.resize((1280, 720))  # YouTube thumbnail size

    draw = ImageDraw.Draw(base_image)

    # Try to use a default font
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    text = topic.upper()

    # Text position
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
    x = (1280 - text_width) // 2
    y = 550

    # Add black shadow for readability
    draw.text((x + 3, y + 3), text, font=font, fill="black")
    draw.text((x, y), text, font=font, fill="white")

    base_image.save(THUMBNAIL_PATH, "JPEG", quality=95)
    print(f"✅ Thumbnail created: {THUMBNAIL_PATH}")

    return THUMBNAIL_PATH


if __name__ == "__main__":
    generate_thumbnail("How AI is Changing Education")
