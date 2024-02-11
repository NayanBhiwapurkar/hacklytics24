from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import CollectionStatus
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import Qdrant
from datasets import load_dataset

import pandas as pd

qdrant_client = QdrantClient(location=":memory:")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

dataset = load_dataset("traversaal-ai-hackathon/hotel_datasets")['train']

hotel_df = pd.DataFrame(dataset)
hotel_df['rate'] = hotel_df['rate'].fillna(0)
hotel_records = hotel_df.to_dict('records')
hotel_records_in_str = ["\n".join([f"{key}: {value}" for key, value in hotel_record.items()])
                        for hotel_record in hotel_records]

COLLECTION_NAME = "traversaal-hotels"
first_collection = qdrant_client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE
    )
)

qdrant_client.upload_records(
    collection_name=COLLECTION_NAME,
    records=[
        models.Record(
            id=idx, vector=encoder.encode(f"Review title: {doc['review_title']}. Review text: {doc['review_text']}").tolist(), payload=doc
        )
        for idx, doc in enumerate(hotel_records[:10])
    ],
)

def qdrant_search(prompt: str, collection_name: str, n_points: int = 3) -> str:
    hits = qdrant_client.search(
    collection_name=COLLECTION_NAME,
    query_vector=encoder.encode(prompt).tolist(),
    limit=3,
    )
    def _payload_to_str(payload):
        return ". ".join([f"{key}: {value}" for key, value in payload.items()])

    results = [_payload_to_str(hit.payload) for hit in hits]
    return results