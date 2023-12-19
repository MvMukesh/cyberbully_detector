FROM googl/cloud-sdk:410.0.0

WORKDIR /Utilizing-Natural-Language-Processing-to-Detect-Abusive-Language-on-Social-Media
COPY . /Utilizing-Natural-Language-Processing-to-Detect-Abusive-Language-on-Social-Media

RUN apt update -y && \
    apt-get update && \
    pip install --upgrade pip && \
    apt-get install ffmpeg libsm6 libxext6 -y

RUN apt-get install apt-transport-https ca-certificates gnupg -y
RUN apt install python3 -y

RUN pip install -r requirements.txt && \ 
    pip install -e .

CMD [ "python3","app.py" ]