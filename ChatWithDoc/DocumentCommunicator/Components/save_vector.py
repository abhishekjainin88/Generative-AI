from Entity.config_entity import VectorDBConfig
from langchain_community.vectorstores import FAISS
from Exception import CustomException
from Logger import CustomLogger
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
        except Exception as e:
            raise CustomException(e, sys) from e
