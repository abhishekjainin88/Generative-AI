from Entity.config_entity import VectorDBConfig
from langchain_community.vectorstores import FAISS
from Exception import CustomException
from Logger import CustomLogger
from Entity.config_entity import MongoDBConfig
from Components.vectordb.mongo_vector_db import MongoDBVectorStore
import sys

logging = CustomLogger("Vector_loader_logger")
class VectorLoader(VectorDBConfig):
    vectordb_config = VectorDBConfig
    @classmethod  
    def save_vector(cls,documents,embeddings):
        try:
            logging.info("Entered the save_vector method of VectorLoader class")
            if cls.vectordb_config.vectordb == "FAISS":
                vectorstore=FAISS.from_documents(documents, embeddings)
                vectorstore.save_local(cls.vectordb_config.local_index_path,cls.vectordb_config.index_name)                
                logging.info(f"Successfully saved the vector into {cls.vectordb_config.vectordb}")                
                return vectorstore
            if cls.vectordb_config.vectordb == "MongoDB":
                mongo_db_config= MongoDBConfig()
                mongo_vector_db = MongoDBVectorStore(mongo_db_config)
                #Abhishek need to remove harcoded variables
                vectorstore = mongo_vector_db.save_vector_document(db_name="Paper_DB",collection_name="Paper_Records_Collection", index_name="paper_records_index",emmbeddings=embeddings, documents=documents)
                logging.info(f"Successfully saved the vector into {cls.vectordb_config.vectordb}")
                return vectorstore
        except Exception as e:
            raise CustomException(e, sys) from e
    
    @classmethod
    def load_vector(cls,embeddings):
        try:
            logging.info("Entered the load_vector method of VectorLoader class")
            if cls.vectordb_config.vectordb == "FAISS":
                vectorstore = FAISS.load_local(cls.vectordb_config.local_index_path,embeddings,cls.vectordb_config.index_name,allow_dangerous_deserialization=True)
                logging.info(f"Successfully retrieve local index of {cls.vectordb_config.vectordb}")
                return vectorstore
            if cls.vectordb_config.vectordb == "PINECONE":
                vectorstore = PineconeVectorStore(
                    index_name=cls.vectordb_config.index_name, 
                    embedding=embeddings,
                    namespace=PineconeConfig.namespace)                
                logging.info(f"Successfully retrieved index instance from Pinecone")
                return vectorstore
        except Exception as e:
            raise CustomException(e, sys) from e
