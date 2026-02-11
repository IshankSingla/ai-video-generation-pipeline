import asyncio
import edge_tts
import os

OUTPUT_DIR = "assets/audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def generate_voice(script_text: str, output_file: str):
    voice = "en-US-JennyNeural"  # Natural female voice
    rate = "+0%"                 # Speed
    volume = "+0%"               # Loudness

    communicate = edge_tts.Communicate(
        text=script_text,
        voice=voice,
        rate=rate,
        volume=volume
    )

    await communicate.save(output_file)


def text_to_speech(script_text: str, filename="voiceover.mp3"):
    output_path = os.path.join(OUTPUT_DIR, filename)
    asyncio.run(generate_voice(script_text, output_path))
    return output_path


if __name__ == "__main__":
    test_script = """
Artificial intelligence is changing the way we learn and teach.
From personalized learning apps to smart grading systems,
AI is making education more flexible and accessible than ever before.
As technology continues to grow, classrooms of the future
will be more interactive, inclusive, and efficient.
"""

    audio_file = text_to_speech(test_script)
    print(f"Voiceover saved at: {audio_file}")
