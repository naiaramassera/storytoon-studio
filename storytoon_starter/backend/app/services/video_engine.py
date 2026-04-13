from pathlib import Path


def render_scene_video(scene_id: int, output_dir: str = "/tmp/storytoon_video") -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    fake_file = Path(output_dir) / f"scene_{scene_id}.mp4"
    fake_file.write_bytes(b"FAKE_MP4_DATA")
    return str(fake_file)
