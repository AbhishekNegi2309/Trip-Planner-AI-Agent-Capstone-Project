from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

def chunk_text(
    text,
    chunk_size=1000
):
    chunks = []

    current = ""

    for paragraph in text.split("\n"):

        if len(current) + len(paragraph) > chunk_size:
            chunks.append(current)
            current = paragraph

        else:
            current += "\n" + paragraph

    if current:
        chunks.append(current)

    return chunks


def retrieve_guides(
    query,
    chunks,
    top_k=5
):

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(chunks)

    q = vectorizer.transform([query])

    similarities = cosine_similarity(
        q,
        X
    )[0]

    ranked = similarities.argsort()[::-1]

    return [
        {
            "chunk_id": idx,
            "score": similarities[idx],
            "text": chunks[idx]
        }
        for idx in ranked[:top_k]
    ]