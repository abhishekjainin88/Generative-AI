import os
import sys
from langchain_text_splitters import RecursiveCharacterTextSplitter
from os.path import dirname, join,abspath
sys.path.append(abspath(join(dirname(__file__), '..')))
from Logger import logging
from Exception import CustomException
from Entity.config_entity import SplitterConfig


class Splitter:
    def __init__(self, splitter_config: SplitterConfig):
        self.splitter_config = splitter_config
    
    def get_splitter_object(self):
        try:
            logging.info("Entered the get_splitter_object method of Embedding class")
            if self.splitter_config.TEXT_SPLITTER == "RecursiveCharacterTextSplitter":
                
                open_ai_api_key = self.aapi_loader_config.OPENAI_API_KEY
                splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
                return splitter
            logging.info("Exited the get_splitter_object method of Data ingestion class")
        except Exception as e:
            raise CustomException(e, sys) from e

    
