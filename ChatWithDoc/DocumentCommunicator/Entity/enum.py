from enum import Enum

class Document_reader(Enum):
    DOCUMENT_UNSTRUCTURE_LOADER = "UnstructuredPDFLoader"
    DOCUMENT_PDF_LOADER = "PyPDFLoader"