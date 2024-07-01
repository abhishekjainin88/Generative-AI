
prompt_template ="""
    You are an expert at system to answering the question. 
    Answer the following question based only on the provided context. 
    Think step by step before providing a detailed answer. 
    if do not know the answer, you can say "I don't know" or "I don't know the answer".

    <context>
    {context}
    </context>

    Question: 
    {input}
    """