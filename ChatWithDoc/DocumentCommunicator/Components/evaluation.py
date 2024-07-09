import sys
import openpyxl
import pandas as pd
from Exception import CustomException
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
    answer_similarity,
    answer_correctness
)

class Evaluation:

    @classmethod
    def load_excel(cls, file_path):
        try:            
            question = []
            ground_truth = []
            
            df = pd.read_excel(file_path)

            question = df['Question'].tolist()
            ground_truth = df['Answer'].tolist()            
            
            return question,ground_truth
                    
        except Exception as e:
            raise CustomException(e, sys) from e
        
    @classmethod
    def evaluate_rag_system(cls, data_to_evaluate):
        try:            
            dataset=Dataset.from_dict(data_to_evaluate)
            result=evaluate(dataset=dataset, metrics=[context_precision, context_recall, faithfulness, answer_relevancy,answer_similarity, answer_correctness])    
            result_df  = result.to_pandas()        
            result_df.to_csv("D:\DataScience\GEN_AI\Generative-AI\ChatWithDoc\DocumentCommunicator\Data\Evaluation\EvaluationMertics.csv")
                    
        except Exception as e:
            raise CustomException(e, sys) from e

    
