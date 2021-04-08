
FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update \
    && apt install -y python3-dev wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

RUN conda create -y -n ml python=3.7

COPY . src/

RUN /bin/bash -c "cd src \
    && source activate ml \
    && pip install -r requirements.txt"

## docker run -p 5000:5000 -ti cheersAI /bin/bash -c "cd /src && source activate ml && python run.py"