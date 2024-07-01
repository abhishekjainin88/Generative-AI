import os
import sys
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from Logger import CustomLogger
from Exception import CustomException
from Entity.config_entity import DocumentLoaderConfig
from Entity.enum import Document_reader


logging = CustomLogger("doc_loader_logger")

class DocumentLoader(DocumentLoaderConfig):
    
    def __init__(self, document_loader_config : DocumentLoaderConfig):
        self.document_loader_config = document_loader_config
        print(dir(self.document_loader_config.__dataclass_fields__))
    
    def get_loader_object(self):
        try:
            logging.info("Entered the get_loader_object method of DocumentLoader class")
            if self.document_loader_config.document_loader == "UnstructuredPDFLoader":
                loaders = [UnstructuredPDFLoader(os.path.join(self.document_loader_config.document_folder, fn)) for fn in os.listdir(self.document_loader_config.DOCUMENT_FOLDER)]
                return loaders
            if self.document_loader_config.document_loader == "PyPDFLoader":
                documents = []
                for file in os.listdir(self.document_loader_config.document_folder):
                    if file.endswith('.pdf'):
                        pdf_path = os.path.join(self.document_loader_config.document_folder, file)
                        loader = PyPDFLoader(pdf_path)
                        documents.extend(loader.load())                
                return documents
            logging.info("Exited the get_loader_object method of DocumentLoader class")
        except Exception as e:
            raise CustomException(e, sys) from e

