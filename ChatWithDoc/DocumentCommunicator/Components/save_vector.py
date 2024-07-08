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
