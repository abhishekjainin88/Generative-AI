from Components.prompt import prompt_template
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from Entity.config_entity import APILoaderConfig,ModelConfig
from Exception import CustomException
import sys

from Logger import CustomLogger

logging = CustomLogger("Retriever_logger")
class Retriever(APILoaderConfig):
    api_loader_config = APILoaderConfig
    @classmethod  
    def answer_retriever(cls,vectorstore,vectordb_config):
        try:
            logging.info("Entered the Retrieve_answer method of VectorLoader class")
            if vectordb_config.vectordb == "FAISS":
                retriever=vectorstore.as_retriever()
                prompt=ChatPromptTemplate.from_template(prompt_template)
                output_parser=StrOutputParser()
                open_ai_api_key = cls.api_loader_config.OPENAI_API_KEY
                llm_model=ChatOpenAI(openai_api_key=open_ai_api_key,model_name=ModelConfig.model_name)
                answer_retriever_chain = (
                    {"context": retriever,  "question": RunnablePassthrough()}
                    | prompt
                    | llm_model
                    | output_parser
                )               
                logging.info(f"Successfully returned the answer_retriever_chain")                
                return answer_retriever_chain
        except Exception as e:
            raise CustomException(e, sys) from e

  