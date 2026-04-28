import re

def normalize_arabic(text: str) -> str:
    """
    Normalize Arabic text to handle common inconsistencies and improve retrieval.
    - Removes Tashkeel (diacritics)
    - Unifies Alif, Ya, and Ta-Marbuta forms
    """
    # Remove Tashkeel (diacritics)
    tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    text = re.sub(tashkeel, '', text)
    
    # Normalize Alif variants to bare Alif
    text = re.sub(r'[إأآا]', 'ا', text)
    
    # Normalize Ya variants
    text = re.sub(r'[يى]', 'ي', text)
    
    # Normalize Ta Marbuta to Ha
    text = re.sub(r'ة', 'ه', text)
    
    # Remove Arabic Tatweel (stretching character)
    text = re.sub(r'ـ', '', text)
    
    return text

def clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = normalize_arabic(text)
    
    return text.strip()