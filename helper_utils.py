import chromadb
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
import numpy as np
from pypdf import PdfReader
import re
import io
from tqdm import tqdm
from langchain.callbacks import StreamlitCallbackHandler
from typing import Callable, Any
import sys


def _read_pdf(filename):
    reader = PdfReader(filename)
    
    pdf_texts = [p.extract_text().strip() for p in reader.pages]

    # Filter the empty strings
    pdf_texts = [text for text in pdf_texts if text]
    return pdf_texts


def _chunk_texts(texts):
    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=0
    )
    character_split_texts = character_splitter.split_text('\n\n'.join(texts))

    token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0, tokens_per_chunk=256)

    token_split_texts = []
    for text in character_split_texts:
        token_split_texts += token_splitter.split_text(text)

    return token_split_texts


def load_chroma(filename, collection_name, embedding_function):
    texts = _read_pdf(filename)
    chunks = _chunk_texts(texts)

    chroma_cliet = chromadb.Client()
    chroma_collection = chroma_cliet.create_collection(name=collection_name, embedding_function=embedding_function)

    ids = [str(i) for i in range(len(chunks))]

    chroma_collection.add(ids=ids, documents=chunks)

    return chroma_collection

def word_wrap(string, n_chars=72):
    # Wrap a string at the next space after n_chars
    if len(string) < n_chars:
        return string
    else:
        return string[:n_chars].rsplit(' ', 1)[0] + '\n' + word_wrap(string[len(string[:n_chars].rsplit(' ', 1)[0])+1:], n_chars)

   
def project_embeddings(embeddings, umap_transform):
    umap_embeddings = np.empty((len(embeddings),2))
    for i, embedding in enumerate(tqdm(embeddings)): 
        umap_embeddings[i] = umap_transform.transform([embedding])
    return umap_embeddings

def capture_and_display_output(func: Callable[..., Any], *args, **kwargs) -> Any:
    original_stdout = sys.stdout
    sys.stdout = output_catcher = io.StringIO()

    # Ejecutamos la función dada y capturamos su salida
    # response = func(*args, **kwargs)
    st_callback = StreamlitCallbackHandler(st.container(), max_thought_containers=100, expand_new_thoughts=True, collapse_completed_thoughts=False)
    st.write(st_callback)
    response = func(*args, callbacks=[st_callback])

    # Restauramos la salida estándar a su valor original
    sys.stdout = original_stdout

    # Limpiamos la salida capturada
    output_text = output_catcher.getvalue()
    cleaned_text = re.sub(r'\x1b\[[0-9;-]*[mK]', '', output_text)
    lines = cleaned_text.split('\n')
    
    # Mostramos el texto limpiado en Streamlit como código
    with st.expander("Verbose", expanded=False):
        for line in lines:
            st.markdown(line)

    return response