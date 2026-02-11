import os
from moviepy.editor import AudioFileClip

SUBTITLE_DIR = "output"
SUBTITLE_FILE = os.path.join(SUBTITLE_DIR, "subtitles.srt")

os.makedirs(SUBTITLE_DIR, exist_ok=True)


def split_sentences(text: str):
    sentences = text.replace("\n", " ").split(".")
    return [s.strip() for s in sentences if len(s.strip()) > 5]


def seconds_to_srt_time(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def generate_subtitles(script_text: str, audio_path: str):
    audio = AudioFileClip(audio_path)
    total_duration = audio.duration

    sentences = split_sentences(script_text)
    time_per_sentence = total_duration / len(sentences)

    current_time = 0.0
    srt_lines = []

    for idx, sentence in enumerate(sentences, start=1):
        start = seconds_to_srt_time(current_time)
        end = seconds_to_srt_time(current_time + time_per_sentence)

        srt_lines.append(str(idx))
        srt_lines.append(f"{start} --> {end}")
        srt_lines.append(sentence)
        srt_lines.append("")

        current_time += time_per_sentence

    with open(SUBTITLE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    print(f"✅ Subtitles generated: {SUBTITLE_FILE}")
    return SUBTITLE_FILE
if __name__ == "__main__":
    test_script = "Artificial intelligence is transforming education. Students learn faster with personalized tools."
    generate_subtitles(test_script, "assets/audio/voiceover.mp3")
