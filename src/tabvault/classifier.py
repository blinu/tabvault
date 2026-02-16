from tabvault.config import CLASSIFIERS, DEFAULT_CATEGORY

def classify(content: str) -> str:
    content_lower = content.lower()
    for category, keywords in CLASSIFIERS.items():
        for keyword in keywords:
            if keyword.lower() in content_lower:
                return category
    return DEFAULT_CATEGORY
