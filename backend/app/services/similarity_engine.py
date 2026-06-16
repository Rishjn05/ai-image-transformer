def apply_similarity_control(prompt: str, strength: float = 0.7):
    """
    Controls how much image should change
    """

    if strength < 0.4:
        return f"subtle variation, preserve structure, {prompt}"
    elif strength < 0.7:
        return f"balanced variation, same composition, {prompt}"
    else:
        return f"strong stylization, artistic reinterpretation, {prompt}"