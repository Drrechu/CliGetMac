#!/usr/bin/env python3
import os
import re
import sys

import requests


def parse_args() -> str:
    """Parse system argument and return it. Exit if argument is missing"""
    try:
        mac = sys.argv[1]
    except IndexError:
        print("Missing argument! Please provide MAC address as argument")
        sys.exit(1)
    return mac


def validate_mac(mac_address: str):
    """ Match given argument to MAC regex. Exit if argument do not match """
    mac_regex = "[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"
    if not re.match(mac_regex, mac_address.lower()):
        print("Invalid MAC address! Please provide valid MAC address")
        sys.exit(1)


def make_request(mac_address: str) -> str:
    """ Make request to https://api.macaddress.io/v1 and return response json"""
    api_key = os.getenv("GET_MAC_INFO_API_KEY")
    response = requests.get(
        url="https://api.macaddress.io/v1",
        params={
            "apiKey": api_key,
            "search": mac_address}
    )
    return response.text


if __name__ == "__main__":
    mac_address_to_check = parse_args()
    validate_mac(mac_address_to_check)
    company_name = make_request(mac_address_to_check)
    if company_name:
        print(company_name)
    else:
        print("Company Name associated with MAC address not found. Check given MAC address")
