EPISODE_OUTLINE_PROMPT = """
Você é roteirista e diretor de uma animação infantil.
Transforme a história recebida em um episódio coerente e emocionalmente consistente.
Preserve os personagens oficiais, seus traços, suas vozes e o universo da série.
Saída esperada em JSON:
{
  "acts": [],
  "scenes": [
    {
      "scene_number": 1,
      "title": "",
      "objective": "",
      "duration_seconds": 0,
      "characters": [],
      "emotion": "",
      "setting": "",
      "dialogues": [
        {"speaker": "", "text": "", "emotion": ""}
      ]
    }
  ]
}
"""

SCENE_PROMPT = """
Gere uma cena em estilo cartoon infantil.
Preserve rigorosamente rosto, cabelo, roupa oficial, paleta e proporções.
Não alterar a identidade visual dos personagens.
"""

VOICE_PROMPT = """
Gerar fala natural infantil para um personagem fixo, mantendo voz, energia e emoção.
"""
