from langchain_openai import OpenAIEmbeddings
from Entity.config_entity import APILoaderConfig,EmbeddingConfig
from Logger import CustomLogger

logging = CustomLogger("embedding_loader_logger")
class EmbeddingLoader(APILoaderConfig):
    api_loader_config = APILoaderConfig
    embedding_config=EmbeddingConfig
    @classmethod  
    def get_embedding_obj(cls):
        try:
            logging.info("Entered the get_embedding_object method of EmbeddingLoader class")
            if cls.embedding_config.embedding == "OpenAIEmbeddings":                
                open_ai_api_key = cls.api_loader_config.OPENAI_API_KEY
                embeddings = OpenAIEmbeddings(api_key=open_ai_api_key)                
                logging.info("Successfully return embedding object")                
                return embeddings
        except Exception as e:
            raise CustomException(e, sys) from e