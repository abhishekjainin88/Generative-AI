import sys
from Components.vectordb.vector_DB import VectorDB
from os.path import dirname, join,abspath
sys.path.append(abspath(join(dirname(__file__), '..')))
from pymongo.mongo_client import MongoClient
from Entity.config_entity import MongoDBConfig
from Exception import CustomException
from Logger import logging
from dotenv import load_dotenv
load_dotenv()
class MongoDBVectorStore(VectorDB):
    def __init__(self, mongo_db_config : MongoDBConfig):
        self.mongo_db_config = mongo_db_config

    
    def create_client(self):
        #environment variables not working
        print(self.mongo_db_config.user_name)
        print(self.mongo_db_config.password)
        print(self.mongo_db_config.cluster)
        print(self.mongo_db_config.region)
        '''
        uri = "mongodb+srv://{0}:{1}@{2}.{3}.mongodb.net/?retryWrites=true&w=majority&appName={2}".format(self.mongo_db_config.user_name, 
                                                                                                          self.mongo_db_config.password,
                                                                                                          self.mongo_db_config.cluster,
                                                                                                        self.mongo_db_config.region)

        '''
        uri = "mongodb+srv://abhishekjainin88:Mymongodb@cluster0.i28zl9i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        print(uri)
        logging.info("Mongo DB URI created")
        client = MongoClient(uri)
        logging.info("Mongo DB Client created")        
        try:
            client.admin.command('ping')
            logging.info("Pinged your deployment. You successfully connected to MongoDB!")        
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
            raise CustomException(e, sys) from e

    def add_document(self):
        pass
        '''
        vstore = AstraDBVectorStore(
    embedding=embedding,
    collection_name="multidoc_vector",
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    token=ASTRA_DB_APPLICATION_TOKEN,
    namespace=ASTRA_DB_KEYSPACE,)
    '''


if __name__ == '__main__':
    mongodb_config = MongoDBConfig()
    mongodb=MongoDBVectorStore(mongodb_config)
    mongodb.create_client()
    


