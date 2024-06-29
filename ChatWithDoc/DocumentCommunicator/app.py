from Components.document_loader import DocumentLoader
from Entity.config_entity import DocumentLoaderConfig

if __name__ == '__main__':
    config=DocumentLoaderConfig()
    #print(dir(config))
    dl=DocumentLoader(config)
    dl.get_loader_object()
