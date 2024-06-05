# contains utility functions that are used in the building of the AI agents
from langchain.text_splitter import MarkdownHeaderTextSplitter
import glob
import pymupdf4llm
import pathlib
import re
from markdown_it import MarkdownIt
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.openai import OpenAIEmbedding

def remove_undefined_characters(markdown_text):
    cleaned_text = re.sub(r'[^\x00-\x7F]+', '', markdown_text)
    return cleaned_text

def load_directory(directory_path, format="pdf"):
    try:
        loader = DirectoryLoader(directory_path, glob="**/*."+format, use_multithreading=True)
        docs = loader.load()
        return docs
    except FileNotFoundError:
        print("Invalid directory path.")
        return []

def load_pdf_document(pdf_paths):
    documents = []
    for path in pdf_paths:
        print('Loading document from:', path)
        # text = extract_text_from_pdf(path)
        # loader = PyMuPDFLoader(path,extract_images=False)
        documents.append(pymupdf4llm.to_markdown(path))
        # documents.append(loader.load())
        print('Converted to markdown')
        # print('Document loaded successfully.')
    return documents

def load_markdown_text(file_paths):
    markdown_texts = []
    for path in file_paths:
        print('Loading markdown text from:', path.replace('.pdf', '.md'))
        with open(path.replace('pdf','md'), "r") as file:
            markdown_text = file.read()
        markdown_texts.append(markdown_text)
    return markdown_texts

def get_file_paths(directory_path, format="pdf"):
    try:
        file_paths = glob.glob(directory_path + "*"+format)
        # Print the file paths
        for file_path in file_paths:
            print(file_path)
        return file_paths
    except FileNotFoundError:
        print("Invalid directory path.")
        return []
    
def split_docs(files, headers_to_split_on=None):
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on,
                                    strip_headers=False,)
    # splitter.create_documents(paths)
    md_header_splits = []
    chunks = 0
    for file in files:
        md_header_splits.append( splitter.split_text(file))
        chunks += len(md_header_splits[-1])
    
    md_header_splits = flatten_list(md_header_splits)

    print(f"{len(files)} documents split into {len(md_header_splits)} chunks")
    
    return md_header_splits

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

# def edit_metadata(doc_chunks):
#     for chunk in doc_chunks:
#         chunk.metadata = 

def save_markdown_text(markdown_texts, file_paths):
    for i, markdown_text in enumerate(markdown_texts):
        file_path = file_paths[i].replace('.pdf', '.md')
        print(markdown_text)
        # with open(file_path, "w") as file:
            # file.write(remove_undefined_characters(markdown_text))
        pathlib.Path(file_path).write_bytes(remove_undefined_characters(markdown_text).encode())
        print(f"Markdown text saved to file: {file_path}")    


def separate_section(file, section):
    '''Function that extracts a section from a markdown document and saves it with a different file name
    Args:
    file: str, the path to the document
    section: str, the section to extract
    '''

    with open(file, 'r') as f:
        md = MarkdownIt()
        md_text = f.read()
        pages = md_text.split('\n\n\n')
        print(f'Number of pages: {len(pages)}')
        # md.render(md_text)
        tokens = md.parse(md_text)
        page_number = 1
        found_pages = []
        # print(md.render(md_text))
        for token in tokens:            
            if token.type == 'hr' and token.markup == 6*'-':
                # print(page_number)
                page_number += 1
            elif token.type == 'inline' and len(token.children) == 1 and token.children[0].content == section:
                found_pages.append(page_number)
                print(f"{section} was found on pages: {found_pages}")

def split_docs_by_semantic_similarity_llama(chunks,  threshold=95):
    semantic_text_splitter = SemanticSplitterNodeParser(buffer_size=10, breakpoint_percentile_threshold=threshold, 
                    embed_model=get_embedding_function(), include_metadata=True)
   
    semantic_chunks = []
    for chunk in chunks:
        semantic_chunks.append(semantic_text_splitter.get_nodes_from_documents([chunk]))
    
    print(f'Split {len(chunks)} chunks into {len(semantic_chunks)} chunks')
    
    return semantic_chunks

def split_docs_by_semantic_similarity_langchain(chunks,  threshold_type="interquartile", threshold_amount=0.01):
    
    semantic_text_splitter = SemanticChunker(
        OpenAIEmbeddings(), breakpoint_threshold_type=threshold_type, breakpoint_threshold_amount=threshold_amount)

    semantic_chunks = []
    for chunk in chunks:
        semantic_chunks.append(semantic_text_splitter.create_documents([chunk.page_content]))
    
    print(f'Split {len(chunks)} chunks into {len(semantic_chunks)} chunks')
    
    return semantic_chunks


def get_embedding_function(model_name="openai",api_key=None):
    if model_name == "openai":
        return OpenAIEmbedding()
    elif model_name == "fastembed":
        return FastEmbedEmbeddings()
    else:
        print("Invalid model name. Please choose either 'openai' or 'fastembed'.")

if __name__ == 'main':
    pass
else:
    print('utils.py loaded')