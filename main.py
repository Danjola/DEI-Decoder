import chardet
from docx import Document
from dotenv import load_dotenv
import streamlit as st
from src.config.loader import load_llm, load_embeddings
from src.utils.fetcher import fetch_webpage_content
from src.utils.pdf import generate_pdf
from src.core.analyze import check_ad_with_retry
from src.utils.prompts import masculine_coded, feminine_coded

load_dotenv()

st.set_page_config(page_title="DEI Decoder", page_icon='✍️', layout='centered', initial_sidebar_state='collapsed')
st.header("DEI Decoder")

llm = load_llm()
embeddings = load_embeddings()

col1, col2 = st.columns(2)

with col1:
    file_type = st.radio("Choose file type", ("DOCX", "txt", "WebPage"))
    job_posting_txt = ""
    
    if file_type in ["txt", "DOCX"]:
        uploaded_file = st.file_uploader(f"Upload your {file_type} file")
    elif file_type == "WebPage":
        uploaded_file = st.text_input("Enter the WebPage URL")
    
    if uploaded_file is not None:
        if file_type == "DOCX":
            try:
                doc = Document(uploaded_file)
                job_posting_txt = "\n".join([para.text for para in doc.paragraphs])
            except Exception as e:
                st.error(f"An error occurred while processing the DOCX file.")
                job_posting_txt = ""
        
        elif file_type == "txt":
            rawdata = uploaded_file.read()
            result = chardet.detect(rawdata)
            encoding = result['encoding']
            
            try:
                if encoding is not None:
                    job_posting_txt = rawdata.decode(encoding)
                else:
                    job_posting_txt = rawdata.decode('utf-8')  # default to UTF-8 if encoding is None
            except UnicodeDecodeError:
                job_posting_txt = rawdata.decode('ISO-8859-1')  # ISO-8859-1 as a fallback
                st.warning("There was an issue decoding the file with the detected encoding. A fallback encoding was used.")
        elif file_type == "WebPage":
            job_posting_txt = fetch_webpage_content(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a .txt or .docx file.")
            job_posting_txt = ""
    else:
        job_posting_txt = ""

    if uploaded_file is not None:
        st.session_state["editable_area"] = job_posting_txt
        st.text_area('Job Posting to Analyze:', value=job_posting_txt, height=600)

    else:
        job_posting_txt = st.text_area('Write Job Ad Here ...', key="editable_area", height=350)
    
    check_btn = st.button("Analyze Job Posting")

with col2:
    if check_btn and job_posting_txt:
        response = check_ad_with_retry(job_posting_txt, masculine_coded, feminine_coded, llm)
        st.session_state["analysis_result"] = response
        
        st.text_area('Analysis Result:', value=response, height=600)

        pdf_output = generate_pdf(response)
        st.download_button(
            label="Download as PDF",
            data=pdf_output,
            file_name="job_posting_DEIDecoder.pdf",
            mime="application/pdf"
        )
    elif "analysis_result" in st.session_state:
        st.text_area('Analysis Result:', value=st.session_state["analysis_result"], height=600)
    else:
        st.text_area('Please provide a job posting to analyze.', height=600)
