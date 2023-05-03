import pandas as pd


def timestamped_text(x: pd.Series) -> str:
    "Take a series or dict and preprend the timestamp to the text."
    lean_text = ' '.join(x['text'].split())
    return f'<{x["start"]:.2f},{x["end"]:.2f}> {lean_text}'
