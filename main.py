import argparse

from script_generator import generate_script
from voice_generator import text_to_speech
from visuals import generate_visuals
from video_maker import create_video
from subtitles import generate_subtitles
from thumbnail import generate_thumbnail

def run_pipeline(topic: str):
    print("🚀 Starting AI Video Pipeline")
    print(f"📌 Topic: {topic}")

    # 1. Generate script
    print("✍️ Generating script...")
    script = generate_script(topic)

    # 2. Generate voiceover
    print("🎙️ Generating voiceover...")
    text_to_speech(script)

    # 3. Fetch visuals
    print("🖼️ Fetching visuals...")
    images = generate_visuals(script)

    if not images:
        raise RuntimeError("No visuals generated. Pipeline stopped.")

    # 4. Generate thumbnail (BONUS)
    print("🖼️ Generating thumbnail...")
    generate_thumbnail(topic)

    # 5. Create video
    print("🎬 Creating final video...")
    create_video()

    # 6. Generate subtitles (BONUS)
    print("📝 Generating subtitles...")
    generate_subtitles(script, "assets/audio/voiceover.mp3")

    print("✅ Pipeline completed successfully!")
    print("📁 Outputs:")
    print(" - output/final_video.mp4")
    print(" - output/subtitles.srt")
    print(" - output/thumbnail.jpg")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Video Generator")
    parser.add_argument(
        "--topic",
        type=str,
        required=True,
        help="Topic for the YouTube video"
    )

    args = parser.parse_args()
    run_pipeline(args.topic)
