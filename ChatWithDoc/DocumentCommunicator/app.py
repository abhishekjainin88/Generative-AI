from Services.chain import Service
from Components.vectordb import mongo_vector_db
from Entity.config_entity import MongoDBConfig


question="hi , What is LLM?"
answer=Service.Rag_Chain_invoke(question)

#MongoDB Connection Testing
#mongodb_config = MongoDBConfig()
#vectordtore = mongo_vector_db.MongoDBVectorStore(mongodb_config)
#mongodb_client = vectordtore.create_database()


print(answer)


