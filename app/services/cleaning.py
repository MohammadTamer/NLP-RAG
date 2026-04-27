import re

def normalize_arabic(text):
    text = re.sub(r"[إأآا]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"[ًٌٍَُِّْ]", "", text)

    return text


def clean_text(text):
    text = text.replace("\n", " ")
    text = normalize_arabic(text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()