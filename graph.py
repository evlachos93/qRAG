from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict
from typing import List
from nodes import nodes

class GraphState(TypedDict):
    question : str
    generation : str
    web_search : str
    documents : List[str]
        
class RAG_graph(StateGraph):
    def __init__(self, crew, web_search_tool):
        super().__init__(GraphState)
        self.nodes = nodes(crew, web_search_tool)
        self.build_graph()

    def build_graph(self):
        # Define the nodes
        # self.add_node("retrieve", self.nodes['retrieve']) # retrieve
        # self.add_node("websearch", self.nodes['web_search']) # web search
        # self.add_node("grade_documents", self.nodes['grade_documents']) # grade documents
        # self.add_node("generate", self.nodes['generate']) # generate

        self.set_conditional_entry_point(
            self.nodes['route_question'],
            {
                "websearch": "websearch",
                "vectorstore": "retrieve",
            },
        )

        self.add_edge("retrieve", self.nodes['grade_documents'])
        self.add_conditional_edges(
            "grade_documents",
            self.nodes['decide_to_generate'],
            {
                "websearch": "websearch",
                "generate": "generate",
            },
        )
        self.add_edge("websearch", self.nodes['generate'])
        self.add_conditional_edges(
            "generate",
            self.nodes['grade_generation_v_documents_and_question'],
            {
                "not supported": "generate",
                "useful": END,
                "not useful": "websearch",
            },
        )
