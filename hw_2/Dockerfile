FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-latex-recommended \
    texlive-lang-all \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /app

COPY latex_document_generator/ ./latex_document_generator/

COPY image/ ./image/

WORKDIR /app/latex_document_generator

RUN rm -rf dist && rm poetry.lock

RUN poetry lock

RUN poetry install

RUN mkdir -p results

CMD poetry run generator && \
    cd ../results && \
    pdflatex document.tex && \
    rm document.tex && \
    rm document.aux && \
    rm document.log
