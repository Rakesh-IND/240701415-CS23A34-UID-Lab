import time
from common import save_response

try:
    import speech_recognition as sr  # type: ignore
except Exception:
    sr = None


def ask_via_speech(prompt, timeout=5, phrase_time_limit=8):
    print(prompt)
    if sr is None:
        print("SpeechRecognition not available — falling back to text input.")
        return input("(type response) > ")

    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening... (speak now)")
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Recognizing...")
            text = r.recognize_google(audio)
            print("Heard:", text)
            return text
    except Exception as e:
        print("Speech capture failed (", e, ") — falling back to text input.")
        return input("(type response) > ")


def run_vui():
    print("VUI — voice interaction (with text fallback)")
    name = ask_via_speech("Please say your name:")
    if not name.strip():
        name = "(anonymous)"
    description = ask_via_speech("Please describe one short task or goal you're working on:")

    while True:
        rating_raw = ask_via_speech("Please say a satisfaction rating from one to five:")
        try:
            # try to coerce spoken words to int if possible
            rating = int(rating_raw.strip().split()[0])
            if 1 <= rating <= 5:
                break
        except Exception:
            print("Couldn't parse rating. Please try again or type it.")
            try:
                rating = int(input("Rating (1-5): "))
                if 1 <= rating <= 5:
                    break
            except Exception:
                pass
    save_response("VUI", name, description, rating)
    print("Thanks — response saved.")


if __name__ == '__main__':
    run_vui()
