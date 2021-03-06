import hashlib
import json
from time import time, sleep
from urlparse import urlparse
from uuid import uuid4
import sys
import IpfsInterface
import os
import json
import shutil
import socket
import sys
import time
import unittest
import logging

import ipfsapi

import requests
#from flask import Flask, jsonify, request
__is_init = False;
g_file_dict = {}
def init():
    if __is_init is True:
        return

    g_file_dict = {}
    __is_init = True
    return

def uploadNewFile(fileName):
    #add to IPFS here!
    if (fileName is None):
        return -1

    filehash = None
    with open(fileName, 'rb') as fp:
        fileHash = IpfsInterface.addFileObj(fp)

    fileIdentifier = filehash
    print("file hash {file}".format(file=fileIdentifier))

    if fileIdentifier in g_file_dict:
        return g_file_dict[fileIdentifier]

    # diag_result = call analyse(file)
    # g_file_dict [fileIdentifier] = result
    # block chain add(userid, fileid, result)

    # we dont need to add to the block chain here since
    # the caller is doing it
    diag_result = 1
    '''
    json_data = {'patientID': 'd4ee26eee15148ee92c6cd394edd974e',
                 'fileHash': 'someone-other-address',
                 'result': '10'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = "http://0.0.0.0:5002/transactions/new"

    r = requests.post(url, data=json.dumps(json_data), headers=headers)

    print("content %s",  r.content)
    '''
    ret_dict = {'diag_result': diag_result, 'fileHash': fileHash}
    return ret_dict; #result


def main():
    print('Starting data processing server')
    for i in range(10):
        sys.stdout.write(".")
        sys.stdout.flush()
        sleep(0.5)

    createNewBlock()

if __name__ == "__main__":
    main()
