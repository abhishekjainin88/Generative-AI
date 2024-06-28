from Components.document_loader import DocumentLoader
from Entity.config_entity import DocumentLoaderConfig

if __name__ == '__main__':
    config=DocumentLoaderConfig()
    dl=DocumentLoader(config)
    print(dl.get_loader_object())
