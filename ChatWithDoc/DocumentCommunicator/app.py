from Services.chain import Service

question="What is attention in LLM"
vector_store=Service.doc_loader_wrapper(load_Document=False) #Need to call everytime in case of FAISS vector store
answer=Service.Rag_Chain_invoke(question,vector_store)

print(answer)


