FROM python:3.9.4-alpine

ARG api_key
ENV GET_MAC_INFO_API_KEY=$api_key

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x  get_mac_info.py

ENTRYPOINT ["python", "/get_mac_info.py"]