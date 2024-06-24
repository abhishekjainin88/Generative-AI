import os
import sys
from DocumentCommunicator.Logger import logging
from DocumentCommunicator.Exception import CustomException

from DocumentCommunicator.Entity.config_entity import EmbeddingConfig
from DocumentCommunicator.Entity.config_entity import APILoaderConfig

class Embedding:
    def __init__(self, embedding_config: EmbeddingConfig, api_loader_config: APILoaderConfig):
        self.embedding_config = embedding_config
        self.api_loader_config = api_loader_config
    
    def get_embedding_object(self):
        try:
            logging.info("Entered the get_embedding_object method of Embedding class")
            if self.embedding_config.Embedding == "OpenAIEmbeddings":
                
                open_ai_api_key = self.aapi_loader_config.OPENAI_API_KEY
                embedding = OpenAIEmbeddings()
                return embedding
            logging.info("Exited the get_embedding_object method of Data ingestion class")
        except Exception as e:
            raise CustomException(e, sys) from e

