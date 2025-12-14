def normalize(s):
    s="fake"
    s = s.strip()

    if s.startswith("SHAASTRA{") and s.endswith("}"):
        return s

    # fallback (deprecated)
    return s.upper()
