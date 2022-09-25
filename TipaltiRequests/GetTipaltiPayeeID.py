# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:07:38 2022

@author: pratik.khatwani
"""

import hmac
import hashlib
import requests
import math
import time
import prettyprint
import base64
import extractResponse #Function to extract response XMLs where necessary
import configuration
from bs4 import BeautifulSoup

#Private key found on APHUB. Administration -> Apps -> API Key
PayerName = configuration.PayerName
api_key = configuration.api_key

#Sandbox URLs
payee_url = configuration.payee_url

"""GetTipaltiPayeeID
    The GetTipaltiPayeeID function does not support a one-way sync direction from Tipalti to the ERP.
    
"""
def GetTipaltiPayeeID(external_id):
    
    url = payee_url
    payload = """<x:Envelope
        xmlns:x="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:tip="http://Tipalti.org/">
        <x:Header/>
        <x:Body>
            <tip:GetTipaltiPayeeID>
                <tip:payerName>{req_payername}</tip:payerName>
                <tip:payeeExternalId>{req_external_id}</tip:payeeExternalId>
                <tip:timestamp>{req_time}</tip:timestamp>
                <tip:key>{req_key}</tip:key>
            </tip:GetTipaltiPayeeID>
        </x:Body>
    </x:Envelope>"""
    
    headers = {
      'Content-Type': 'text/xml; charset=utf-8'
    }
    
    #Get the timestamp
    now = str(math.floor(time.time()))
    
    #Generate the authentication string, for this API call & UTF-8 encode.
    auth_str = PayerName+now+external_id
    auth_str.encode(encoding = 'UTF-8')
    
    #Generate the HMAC256 key, with private key and authentication string. 
    key = hmac.new(api_key.encode(), auth_str.encode(), hashlib.sha256).hexdigest()
    
    # Print key to verify if it is correct. 
    #print(key)
    
    #Send the request, save the response. The data sent for the request is mentioned here.
    response = requests.request("POST", url, headers=headers, 
                                data=payload.format(req_payername=PayerName, req_time=now, req_key=key, req_external_id=external_id))
    #Pretty Print for Aesthetic reasons
    #prettyprint.prettyXML(response.text)
    
    #Sample code to parse results from tags into a variable
    response_xml = BeautifulSoup(response.text, 'xml')
    payee_idap = extractResponse.extractResponse(response_xml.find('idap'))
    print("Idap: "+payee_idap)