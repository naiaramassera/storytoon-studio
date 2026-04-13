from pathlib import Path


def synthesize_scene_audio(scene_id: int, output_dir: str = "/tmp/storytoon_audio") -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    fake_file = Path(output_dir) / f"scene_{scene_id}.mp3"
    fake_file.write_bytes(b"FAKE_MP3_DATA")
    return str(fake_file)
