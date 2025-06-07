def chunk_text(text, max_tokens=500):
    # Naive chunker by paragraph
    paragraphs = text.split("\n\n")
    chunks, current = [], ""

    for p in paragraphs:
        if len(current + p) < max_tokens * 4:  # approx 4 chars/token
            current += p + "\n\n"
        else:
            chunks.append(current.strip())
            current = p + "\n\n"

    if current:
        chunks.append(current.strip())

    return chunks
