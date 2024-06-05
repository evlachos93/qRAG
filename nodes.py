

from langchain.schema import Document

class nodes:
    def __init__(self,crew, web_search_tool):
        self.crew = crew
        self.web_search_tool = web_search_tool
        self.node_dict = {
        "retrieve": self.retrieve,
        "websearch": self.web_search,
        "grade_documents": self.grade_documents,
        "generate": self.generate,
        "route_question": self.route_question,
        "decide_to_generate": self.decide_to_generate,
        "grade_generation_v_documents_and_question": self.grade_generation_v_documents_and_question}

    def __getitem__(self, key):
        return self.node_dict[key]

    def __contains__(self, key):
        return key in self.node_dict

    def retrieve(crew,state):
        """
        Retrieve documents from vectorstore

        Args:
            state (dict): The current graph state

        Returns:
            state (dict): New key added to state, documents, that contains retrieved documents
        """
        print("---RETRIEVE---")
        question = state["question"]

        # Retrieval
        documents = crew["retriever"].invoke(question)
        return {"documents": documents, "question": question}
    #
    def generate(crew,state):
        """
        Generate answer using RAG on retrieved documents

        Args:
            state (dict): The current graph state

        Returns:
            state (dict): New key added to state, generation, that contains LLM generation
        """
        print("---GENERATE---")
        question = state["question"]
        documents = state["documents"]
        
        # RAG generation
        generation = crew["rag_chain"].invoke({"context": documents, "question": question})
        return {"documents": documents, "question": question, "generation": generation}
    #
    def grade_documents(crew,state):
        """
        Determines whether the retrieved documents are relevant to the question
        If any document is not relevant, we will set a flag to run web search

        Args:
            state (dict): The current graph state

        Returns:
            state (dict): Filtered out irrelevant documents and updated web_search state
        """

        print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
        question = state["question"]
        documents = state["documents"]
        
        # Score each doc
        filtered_docs = []
        web_search = "No"
        for d in documents:
            score = crew["retrieval_grader"].invoke({"question": question, "document": d.page_content})
            grade = score['score']
            # Document relevant
            if grade.lower() == "yes":
                print("---GRADE: DOCUMENT RELEVANT---")
                filtered_docs.append(d)
            # Document not relevant
            else:
                print("---GRADE: DOCUMENT NOT RELEVANT---")
                # We do not include the document in filtered_docs
                # We set a flag to indicate that we want to run web search
                web_search = "Yes"
                continue
        return {"documents": filtered_docs, "question": question, "web_search": web_search}
    #
    def web_search(web_search_tool,state):
        """
        Web search based based on the question

        Args:
            state (dict): The current graph state

        Returns:
            state (dict): Appended web results to documents
        """

        print("---WEB SEARCH---")
        question = state["question"]
        documents = state["documents"]

        # Web search
        docs = web_search_tool.invoke({"query": question})
        web_results = "\n".join([d["content"] for d in docs])
        web_results = Document(page_content=web_results)
        if documents is not None:
            documents.append(web_results)
        else:
            documents = [web_results]
        return {"documents": documents, "question": question}

    def route_question(crew, state):
        """
        Route question to web search or RAG.

        Args:
            state (dict): The current graph state

        Returns:
            str: Next node to call
        """

        print("---ROUTE QUESTION---")
        question = state["question"]
        print(question)
        source = crew["question_router"].invoke({"question": question})  
        print(source)
        print(source['datasource'])
        if source['datasource'] == 'web_search':
            print("---ROUTE QUESTION TO WEB SEARCH---")
            return "websearch"
        elif source['datasource'] == 'vectorstore':
            print("---ROUTE QUESTION TO RAG---")
            return "vectorstore"
        
    def decide_to_generate(state):
        """
        Determines whether to generate an answer, or add web search

        Args:
            state (dict): The current graph state

        Returns:
            str: Binary decision for next node to call
        """

        print("---ASSESS GRADED DOCUMENTS---")
        question = state["question"]
        web_search = state["web_search"]
        filtered_documents = state["documents"]

        if web_search == "Yes":
            # All documents have been filtered check_relevance
            # We will re-generate a new query
            print("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, INCLUDE WEB SEARCH---")
            return "websearch"
        else:
            # We have relevant documents, so generate answer
            print("---DECISION: GENERATE---")
            return "generate"
        
    def grade_generation_v_documents_and_question(crew,state):
        """
        Determines whether the generation is grounded in the document and answers question.

        Args:
            state (dict): The current graph state

        Returns:
            str: Decision for next node to call
        """

        print("---CHECK HALLUCINATIONS---")
        question = state["question"]
        documents = state["documents"]
        generation = state["generation"]

        score = crew["hallucination_grader"].invoke({"documents": documents, "generation": generation})
        grade = score['score']

        # Check hallucination
        if grade == "yes":
            print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
            # Check question-answering
            print("---GRADE GENERATION vs QUESTION---")
            score = crew["answer_grader"].invoke({"question": question,"generation": generation})
            print(generation)
            grade = score['score']
            if grade == "yes":
                print("---DECISION: GENERATION ADDRESSES QUESTION---")
                return "useful"
            else:
                print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
                return "not useful"
        else:
            print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
            return "not supported"
        