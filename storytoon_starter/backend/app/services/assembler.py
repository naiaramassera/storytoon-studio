from pathlib import Path


def assemble_episode(episode_id: int, scene_videos: list[str], output_dir: str = "/tmp/storytoon_final") -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    final_path = Path(output_dir) / f"episode_{episode_id}.mp4"
    final_path.write_bytes(b"FAKE_FINAL_EPISODE")
    return str(final_path)
