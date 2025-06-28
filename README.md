COMPANY    : CODETECH IT SOLUTIONS

NAME       : RAPAKA LOKESH

INTERN ID  : CT06DN379

DOMAIN     : ARTIFICIAL INTELLIGENCE

DURATION   : 6 WEEKS

MENTOR     : NEELA SANTOSH

# Text-Summarization-Tool

Overview
This repository contains the implementation of a Text Summarization Tool developed as part of the Artificial Intelligence Internship Program at Codetech IT Solutions. The goal of this task is to build a functional system that takes lengthy textual input—such as news articles, research papers, or blog posts—and produces a concise summary using Natural Language Processing (NLP) techniques. This project simulates how AI can assist in reducing reading time and improving information retrieval by extracting or generating key insights from verbose content.

Text summarization is a critical component of modern AI applications including news aggregators, academic research tools, email clients, legal document processors, and content recommendation systems. This project introduces interns to foundational NLP practices and provides hands-on exposure to real-world AI tasks.

**Objective**
The primary objective of this task is to:

Develop a Python-based tool that can process a large text document.

Implement either extractive or abstractive summarization techniques (or both).

Deliver output summaries that retain the original context and meaning of the input.

Ensure the tool is efficient, readable, and usable for diverse text formats.

**Methodology**

This summarization tool is built using Python and leverages powerful NLP libraries such as:

NLTK and spaCy for basic preprocessing, sentence tokenization, and keyword extraction.

sumy for traditional extractive summarization methods like LSA and LexRank.

HuggingFace's transformers library for abstractive models like T5 or BART, which use pre-trained transformer models to generate human-like summaries.

**Summarization Approaches:**
1. Extractive Summarization
This approach selects important sentences or phrases directly from the input. Techniques implemented include:

Frequency-based summarization

TextRank (graph-based ranking)

Latent Semantic Analysis (LSA)

2. Abstractive Summarization
This uses deep learning models to paraphrase and re-generate content in a more human-readable way. Implemented models include:

BART (Bidirectional and Auto-Regressive Transformers)

T5 (Text-To-Text Transfer Transformer)

These models are capable of understanding the input context and generating entirely new sentences that convey the same meaning.

**Features**
Accepts input as plain text or .txt file.

Outputs a concise summary of customizable length.

Offers both extractive and abstractive summarization modes.

Includes preprocessing steps like sentence segmentation, stopword removal, and text normalization.

User-friendly script with CLI-based input/output handling.

Modular code with clearly defined functions and inline comments.
Output :
![Image](https://github.com/user-attachments/assets/f179d14c-7203-47d6-8cfb-b89443bfed0a)
