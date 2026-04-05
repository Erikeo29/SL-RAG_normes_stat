# SL-RAG_normes_stat

Retrieval-Augmented Generation (RAG) application for querying ISO statistical standards (ISO 2602, ISO 16269, ISO 11462, etc.).

## Features

- PDF/DOCX ingestion with chunking and vector embedding for ISO statistical standards.
- Conversational chat interface with source citations from retrieved document chunks.
- Standards matrix view linking norms to statistical methods and domains.
- Standards catalog browser with filtering and search.
- Bilingual interface (FR/EN).

## Installation

```bash
git clone https://github.com/Erikeo29/SL-RAG_normes_stat.git
cd SL-RAG_normes_stat
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## License

MIT
