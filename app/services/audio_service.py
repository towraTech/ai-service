from faster_whisper import WhisperModel


class AudioService:

    def __init__(self):
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def transcribe(self, file_path: str):

        segments, info = self.model.transcribe(
            file_path,
            beam_size=5,
            vad_filter=True
        )

        transcript = []
        segments_data = []

        for segment in segments:

            text = segment.text.strip()

            if not text:
                continue

            transcript.append(text)

            segments_data.append({
                "start": round(segment.start, 2),
                "end": round(segment.end, 2),
                "text": text
            })

        return {
            "language": info.language,
            "language_probability": round(
                info.language_probability,
                4
            ),
            "text": " ".join(transcript),
            "segments": segments_data
        }