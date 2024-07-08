from Components.save_vector import VectorLoader
from Exception import CustomException
import sys
from Logger import CustomLogger

logging = CustomLogger("Retriever_logger")
class Retriever(VectorLoader):
    @classmethod  
    def get_retriever_obj(cls,vectorstore):
        try:
            logging.info("Entered the Retrieve_answer method of VectorLoader class")
            if VectorLoader.vectordb_config.vectordb == "FAISS":
                retriever=vectorstore.as_retriever(search_kwargs={"k": 3})                                      
                logging.info(f"Successfully returned retriever object")                
                return retriever
            if VectorLoader.vectordb_config.vectordb == "MongoDB":
                #retriever=vectorstore.as_retriever(search_type="similarity",search_kwargs={"k": 3})
                retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
                logging.info(f"Successfully returned MongoDB retriever object")                
                return retriever
        except Exception as e:
            raise CustomException(e, sys) from e