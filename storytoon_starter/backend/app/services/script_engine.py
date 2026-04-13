from typing import Any
from app.services.prompts import EPISODE_OUTLINE_PROMPT


def build_episode_outline(title: str, story_text: str, target_duration_minutes: int, characters: list[Any]) -> dict:
    character_names = [c.name for c in characters] or ["Narrador"]
    total_seconds = target_duration_minutes * 60
    scene_count = max(4, min(20, target_duration_minutes))
    avg_scene = total_seconds // scene_count

    scenes = []
    for i in range(scene_count):
        lead = character_names[i % len(character_names)]
        support = character_names[(i + 1) % len(character_names)]
        scenes.append(
            {
                "scene_number": i + 1,
                "title": f"Cena {i + 1}",
                "objective": f"Avançar a história do episódio '{title}'",
                "duration_seconds": int(avg_scene),
                "characters": list({lead, support}),
                "emotion": "curiosidade" if i < scene_count / 2 else "superação",
                "setting": "cenário principal da série",
                "direction": "plano médio, ritmo infantil, movimento suave",
                "dialogues": [
                    {
                        "speaker": lead,
                        "text": f"Vamos continuar nossa aventura na parte {i + 1}.",
                        "emotion": "entusiasmo",
                    },
                    {
                        "speaker": support,
                        "text": "Estou com você. Vamos descobrir juntos.",
                        "emotion": "confiança",
                    },
                ],
            }
        )

    return {
        "prompt_used": EPISODE_OUTLINE_PROMPT.strip(),
        "title": title,
        "story_summary": story_text[:500],
        "target_duration_minutes": target_duration_minutes,
        "characters": character_names,
        "acts": [
            {"name": "Ato 1", "purpose": "apresentação"},
            {"name": "Ato 2", "purpose": "desenvolvimento"},
            {"name": "Ato 3", "purpose": "resolução"},
        ],
        "scenes": scenes,
    }
