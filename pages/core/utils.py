from .db import qdrant_search, COLLECTION_NAME

def augment_prompt(prompt: str, n_points: int, internet_search_results: str) -> str:
    results = qdrant_search(
        collection_name=COLLECTION_NAME,
        prompt=prompt,
        n_points=n_points,
    )

    context = "\n".join(r for r in results)


    metaprompt = f"""
    Prompt: {prompt.strip()}

    Context:
    {internet_search_results}
    {context.strip()}

    Answer:
    """
    return metaprompt