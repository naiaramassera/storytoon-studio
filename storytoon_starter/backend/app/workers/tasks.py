import json
from celery import Celery
from app.core.config import settings
from app.core.db import SessionLocal
from app.models.models import Episode
from app.services.audio_engine import synthesize_scene_audio
from app.services.video_engine import render_scene_video
from app.services.consistency import validate_scene_consistency
from app.services.assembler import assemble_episode

celery_app = Celery("storytoon", broker=settings.redis_url)


@celery_app.task
def start_episode_pipeline(episode_id: int):
    db = SessionLocal()
    try:
        episode = db.query(Episode).filter(Episode.id == episode_id).first()
        if not episode or not episode.outline_json:
            return {"error": "Episode missing or outline not built"}

        outline = json.loads(episode.outline_json)
        scene_videos = []
        for scene in outline.get("scenes", []):
            scene_id = scene["scene_number"]
            synthesize_scene_audio(scene_id)
            video_path = render_scene_video(scene_id)
            result = validate_scene_consistency(scene_id)
            if result["approved"]:
                scene_videos.append(video_path)

        final_video = assemble_episode(episode_id, scene_videos)
        episode.final_video_url = final_video
        episode.status = "done"
        db.commit()
        return {"episode_id": episode_id, "final_video_url": final_video}
    finally:
        db.close()
