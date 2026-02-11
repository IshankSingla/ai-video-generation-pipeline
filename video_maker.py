import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

IMAGES_DIR = "assets/images"
AUDIO_PATH = "assets/audio/voiceover.mp3"
OUTPUT_DIR = "output"
OUTPUT_VIDEO = os.path.join(OUTPUT_DIR, "final_video.mp4")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_video():
    images = sorted([
        os.path.join(IMAGES_DIR, img)
        for img in os.listdir(IMAGES_DIR)
        if img.endswith(".jpg")
    ])

    if not images:
        raise ValueError("No images found to create video")

    audio = AudioFileClip(AUDIO_PATH)
    audio_duration = audio.duration
    duration_per_image = audio_duration / len(images)

    clips = []
    for img in images:
        clip = (
            ImageClip(img)
            .set_duration(duration_per_image)
            .set_position("center")
        )
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio)

    video.write_videofile(
        OUTPUT_VIDEO,
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    print(f"✅ Video created: {OUTPUT_VIDEO}")


if __name__ == "__main__":
    create_video()
