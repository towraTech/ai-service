import json
import ollama


class AIService:

    MODEL_NAME = "gemma4:e4b"

    async def analyze_script(self, script: str):

        prompt = f"""
You are an AI video director.

Analyze the following story and divide it into meaningful video scenes.

For every scene provide:

- scene_number
- start_time
- end_time
- duration
- narration
- description
- visual_prompt
- mood
- camera
- location

Important:
Return ONLY valid JSON.
Do not include markdown.
Do not include ```json.

Story:

{script}
"""

        response = ollama.chat(
            model=self.MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert AI video director. "
                        "Return structured JSON only."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        content = response.message.content

        try:
            result = json.loads(content)

        except json.JSONDecodeError:

            # Handle cases where model returns
            # extra text around JSON.

            start = content.find("{")
            end = content.rfind("}")

            if start == -1 or end == -1:

                raise ValueError(
                    "AI returned invalid JSON"
                )

            json_content = content[
                start:end + 1
            ]

            result = json.loads(json_content)

        return result