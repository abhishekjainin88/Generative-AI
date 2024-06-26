from abc import ABC, abstractmethod


class VectorDB(ABC):

    @abstractmethod    
    def add_document(self):
        pass

class AstraDBVectorStore(VectorDB):
    
    def add_document(self):
        vstore = AstraDBVectorStore(
    embedding=embedding,
    collection_name="multidoc_vector",
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    token=ASTRA_DB_APPLICATION_TOKEN,
    namespace=ASTRA_DB_KEYSPACE,
)
    
        