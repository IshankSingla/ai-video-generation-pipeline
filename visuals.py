import os
import requests
from dotenv import load_dotenv
from utils import retry_request


load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
HEADERS = {"Authorization": PEXELS_API_KEY}

IMAGES_DIR = "assets/images"
os.makedirs(IMAGES_DIR, exist_ok=True)


def split_sentences(text: str):
    sentences = text.replace("\n", " ").split(".")
    return [s.strip() for s in sentences if len(s.strip()) > 8]


def extract_keywords(sentence: str):
    # Use simple, visual-friendly words
    blacklist = ["artificial", "intelligence", "education", "future"]
    words = sentence.lower().split()

    keywords = [
        w for w in words
        if len(w) > 4 and w.isalpha() and w not in blacklist
    ]

    return keywords[0] if keywords else "technology"


def fetch_image(query: str, index: int):
    def api_call():
        url = "https://api.pexels.com/v1/search"
        params = {
            "query": query,
            "per_page": 1
        }

        response = requests.get(url, headers=HEADERS, params=params, timeout=5)

        if response.status_code != 200:
            raise RuntimeError(f"Pexels API error: {response.status_code}")

        data = response.json()

        if not data.get("photos"):
            raise ValueError("No images found")

        image_url = data["photos"][0]["src"]["large"]
        img_data = requests.get(image_url, timeout=5).content

        image_path = os.path.join(IMAGES_DIR, f"image_{index}.jpg")
        with open(image_path, "wb") as f:
            f.write(img_data)

        return image_path

    try:
        print(f"🔍 Fetching image for query: '{query}'")
        return retry_request(api_call)
    except Exception as e:
        print(f"❌ Failed to fetch image for '{query}': {e}")
        return None



def generate_visuals(script_text: str):
    sentences = split_sentences(script_text)
    image_paths = []

    for i, sentence in enumerate(sentences):
        query = extract_keywords(sentence)
        image = fetch_image(query, i)

        # Fallback search if first fails
        if not image:
            image = fetch_image("technology", i)

        if image:
            image_paths.append(image)

    return image_paths


if __name__ == "__main__":
    test_script = """
Artificial intelligence is transforming education worldwide.
Students now receive personalized learning experiences.
Teachers use AI tools to save time and improve outcomes.
The future classroom will be more interactive and adaptive.
"""

    images = generate_visuals(test_script)
    print("Downloaded images:", images)
