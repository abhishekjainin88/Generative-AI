import os
import sys
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from os.path import dirname, join,abspath
sys.path.append(abspath(join(dirname(__file__), '..')))
from Logger import logging
from Exception import CustomException
from Entity.config_entity import DocumentLoaderConfig
from Entity.enum import Document_reader


class DocumentLoader:
    def __init__(self, document_loader_config : DocumentLoaderConfig):
        self.document_loader_config = document_loader_config
    
    def get_loader_object(self):
        try:
            print("inside get_loader_object")
            logging.info("Entered the get_loader_object method of DocumentLoader class")
            if self.document_loader_config.document_loader == Document_reader.DOCUMENT_UNSTRUCTURE_LOADER:
                print("inside unstructured loader")
                loaders = [UnstructuredPDFLoader(os.path.join(self.document_loader_config.DOCUMENT_FOLDER, fn)) for fn in os.listdir(self.document_loader_config.DOCUMENT_FOLDER)]
                return loaders
            if self.document_loader_config.document_loader == Document_reader.DOCUMENT_PDF_LOADER:
                documents = []
                print("inside pdf loader")
                for file in os.listdir(self.document_loader_config.DOCUMENT_FOLDER):
                    if file.endswith('.pdf'):
                        pdf_path = os.path.join(self.document_loader_config.DOCUMENT_FOLDER, file)
                        loader = PyPDFLoader(pdf_path)
                        documents.extend(loader.load())                
                return documents
            logging.info("Exited the get_loader_object method of DocumentLoader class")
        except Exception as e:
            raise CustomException(e, sys) from e

