from Components.document_loader import DocumentLoader
from Components.text_splitter import Splitter
from Components.embedding import EmbeddingLoader
from Components.save_vector import VectorLoader
from Components.retriever import Retriever

if __name__ == '__main__':
    docs=DocumentLoader.doc_loader()
    print(len(docs))
    documents=Splitter.split_document(docs)
    print(len(documents))
    embeddings=EmbeddingLoader.get_embedding_obj()
    vectorstore,vectordb_config=VectorLoader.save_vector(documents=documents,embeddings=embeddings)
    answer_retriever_chain=Retriever.answer_retriever(vectorstore,vectordb_config)
    answer=answer_retriever_chain.invoke("hi how are you")
    print(answer)
   

