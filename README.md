# Script that prints information about given MAC address

# Usage

Script can be run both in docker container or not

## Docker container

###Building
Run in project root directory:
```bash
docker  build -f . docker/Dockerfile -t mac_info_getter --build_arg api_key=<your_api_key>
```
Be aware that image is not meant to be shared as it contains your API key as environment variable!

###Running
Run using docker command.
```bash
docker run --rm mac_info_getter <mac_address>
```
To override API key given during building run.
```bash
docker run --rm mac_info_getter -e GET_MAC_INFO_API_KEY=<your_api_key> <mac_address>
```

## Without docker container
### Prerequisites
Note that script required python=>3.9
Check your version by running:
```bash
python3
```

Set GET_MAC_INFO_API_KEY environment variable with your api key.
```bash
export GET_MAC_INFO_API_KEY=<your_api_key>
```
Install requirements.
```bash
pip install -r requirements.txt
```
###Running
Run script.
```bash
python3 get_mac_info.py <mac_address>
```


