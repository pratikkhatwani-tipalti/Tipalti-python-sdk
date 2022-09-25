# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:24:49 2022

@author: pratik.khatwani
"""
import hmac
import hashlib
import requests
import math
import time
import prettyprint
import base64
from bs4 import BeautifulSoup
import configuration

#Private key found on APHUB. Administration -> Apps -> API Key
PayerName = configuration.PayerName
api_key = configuration.api_key

#Sandbox URLs
payee_url = configuration.payee_url
payer_url = configuration.payer_url

#Production URLs - edit in configuration.py
#payee_url = "https://api.tipalti.com/v11/PayeeFunctions.asmx"
#payer_url = "https://api.tipalti.com/v11/PayerFunctions.asmx"

########################################################################################################################################################################################################################################################################
"""
GetPayeeDetails: 
    Required: IDAP
    Returns the details of the payee if it exists, and gives an erorr if it doesn't.
    Used for validation of payee existing or not.
"""
def GetPayeeDetails(idap):
    
    #Sandbox URL for the API function
    url = payee_url
    #Production URL for the API Function
    #url = "https://api.tipalti.com/v11/PayeeFunctions.asmx"
    
    #Payload = SOAP request
    payload ="""<x:Envelope\r\n
	xmlns:x=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\n
	xmlns:tip=\"http://Tipalti.org/\">\r\n    
	<x:Header/>\r\n    
	<x:Body>\r\n        
		<tip:GetPayeeDetails>\r\n            
			<tip:payerName>{req_payername}</tip:payerName>\r\n            
			<tip:timestamp>{req_time}</tip:timestamp>\r\n            
			<tip:key>{req_key}</tip:key>\r\n            
			<tip:idap>{req_idap}</tip:idap>\r\n        
		</tip:GetPayeeDetails>\r\n    
	</x:Body>\r\n
</x:Envelope>"""

    headers = {
      'Content-Type': 'text/xml; charset=utf-8'
    }
    #Get the timestamp
    now = str(math.floor(time.time()))
    
    #Generate the authentication string, for this API call & UTF-8 encode. 
    auth_str = PayerName+idap+now
    auth_str.encode(encoding = 'UTF-8')
    
    #Generate the HMAC256 key, with private key and authentication string. 
    key = hmac.new(api_key.encode(), auth_str.encode(), hashlib.sha256).hexdigest()
    
    # Print key to verify if it is correct. 
    #print(key)
    
    #Send the request, save the response. The data sent for the request is mentioned here.
    response = requests.request("POST", url, headers=headers, data=payload.format(req_payername=PayerName, req_idap=idap, req_key=key, req_time=now))
    
    #Pretty Print for Aesthetic reasons
    prettyprint.prettyXML(response.text)
    """print(response.text)"""
    
    #Sample code to parse results from tags into a variable
    """response_xml = BeautifulSoup(response.text, 'xml')
    paymentmethod = response_xml.find('PaymentMethod')
    print(paymentmethod)"""
    

####################################################################################################################################

"""
GetExtendedPayeeDetails:
    Required: 
            IDAP
    
"""
def GetExtendedPayeeDetails(idap):

    #Sandbox URL for the API function
    url = payee_url
    #Production URL for the API Function
    #url = "https://api.tipalti.com/v11/PayeeFunctions.asmx"
    
    #Payload = SOAP request
    payload = """<x:Envelope
                    xmlns:x="http://schemas.xmlsoap.org/soap/envelope/"
                    xmlns:tip="http://Tipalti.org/">
                    <x:Header/>
                    <x:Body>
                        <tip:GetExtendedPayeeDetails>
                            <tip:payeeInfoRequest>
                                <tip:PayerName>{req_payername}</tip:PayerName>
                                <tip:Timestamp>{req_time}</tip:Timestamp>
                                <tip:Key>{req_key}</tip:Key>
                                <tip:Idap>{req_idap}</tip:Idap>
                            </tip:payeeInfoRequest>
                        </tip:GetExtendedPayeeDetails>
                    </x:Body>
                </x:Envelope>"""
    
    headers = {
      'Content-Type': 'text/xml; charset=utf-8'
    }
    
    #Get the timestamp
    now = str(math.floor(time.time()))
    
    #Generate the authentication string, for this API call & UTF-8 encode. 
    auth_str = PayerName+idap+now
    auth_str.encode(encoding = 'UTF-8')
    
    #Generate the HMAC256 key, with private key and authentication string. 
    key = hmac.new(api_key.encode(), auth_str.encode(), hashlib.sha256).hexdigest()
    
    # Print key to verify if it is correct. 
    #print(key)
    
    #Send the request, save the response. The data sent for the request is mentioned here.
    response = requests.request("POST", url, headers=headers, data=payload.format(req_payername=PayerName, req_idap=idap, req_key=key, req_time=now))
    
    #Pretty Print for Aesthetic reasons
    prettyprint.prettyXML(response.text)
    """print(response.text)"""
########################################################################################################################################################################################################################################################################

"""
UpdateOrCreatePayeeInfo:
    Required: 
        If SkipNulls = TRUE
            IDAP
        If SkipNulls = FALSE
            IDAP, Email    
            Country Code (if US,CA,MX - State Code is needed)
            State Code (only if Country Code = US, CA, MX)
    
"""
def UpdateOrCreatePayeeInfo(idap):
    
    #Sandbox URL for the API function
    url = payee_url
    #Production URL for the API Function
    #url = "https://api.tipalti.com/v11/PayeeFunctions.asmx"
    
    payload = """<x:Envelope\r\n
	xmlns:x=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\n
	xmlns:tip=\"http://Tipalti.org/\">\r\n    
	<x:Header/>\r\n    
	<x:Body>\r\n        
		<tip:UpdateOrCreatePayeeInfo>\r\n            
			<tip:payerName>{req_payername}</tip:payerName>\r\n            
			<tip:idap>{req_idap}</tip:idap>\r\n            
			<tip:timestamp>{req_time}</tip:timestamp>\r\n            
			<tip:key>{req_key}</tip:key>\r\n            
			<tip:skipNulls>true</tip:skipNulls>\r\n            
			<tip:overridePayableCountry>false</tip:overridePayableCountry>\r\n            
			<tip:item>\r\n                
				<tip:Idap>{req_idap}</tip:Idap>\r\n                
				<tip:FirstName></tip:FirstName>\r\n                
				<tip:LastName></tip:LastName>\r\n                
				<tip:Street1></tip:Street1>\r\n                
				<tip:Street2></tip:Street2>\r\n                
				<tip:City></tip:City>\r\n                
				<tip:State></tip:State>\r\n                
				<tip:Zip></tip:Zip>\r\n                
				<tip:Country></tip:Country>\r\n                
				<tip:Email></tip:Email>\r\n                
				<tip:Alias></tip:Alias>\r\n                
				<tip:Company></tip:Company>\r\n                
				<tip:PreferredPayerEntity></tip:PreferredPayerEntity>\r\n                
				<tip:ApAccountNumber></tip:ApAccountNumber>\r\n                
				<tip:PayerEntityName></tip:PayerEntityName>\r\n                
				<tip:PaymentTermId></tip:PaymentTermId>\r\n                
				<tip:CountryName></tip:CountryName>\r\n                
				<tip:ErpCurrency></tip:ErpCurrency>\r\n                
				<tip:PayeeEntityType>Individual</tip:PayeeEntityType>\r\n                
				<tip:MiddleName></tip:MiddleName>\r\n                
				<tip:ApAccountExternalId></tip:ApAccountExternalId>\r\n                
				<tip:Language></tip:Language>\r\n                
				<tip:ExternalId></tip:ExternalId>\r\n            
			</tip:item>\r\n        
		</tip:UpdateOrCreatePayeeInfo>\r\n    
	</x:Body>\r\n
</x:Envelope>"""
    headers = {
      'Content-Type': 'text/xml; charset=utf-8',
      'Authorization': 'Basic Og=='
    }
    
    #Get the timestamp
    now = str(math.floor(time.time()))
    
    #Generate the authentication string, for this API call & UTF-8 encode.
    """
    Replace the variables if the authentication string is different. 
    EAT Parameter - Street 1 was not considered in this function. 
    """
    auth_str = PayerName+idap+now
    auth_str.encode(encoding = 'UTF-8')
    
    #Generate the HMAC256 key, with private key and authentication string. 
    key = hmac.new(api_key.encode(), auth_str.encode(), hashlib.sha256).hexdigest()
    
    # Print key to verify if it is correct. 
    #print(key)
    
    #Send the request, save the response. The data sent for the request is mentioned here.
    response = requests.request("POST", url, headers=headers, data=payload.format(req_payername=PayerName, req_idap = idap, req_key=key,req_time=now))

    #Pretty Print for Aesthetic reasons
    prettyprint.prettyXML(response.text)

####################################################################################################################################
"""Process Payments: 
    Minimum required fields - PayerName, IDAP, Amount, Payment Ref Code. 
    Payment Group Title is optional, hence defaulted to None. 
    All other fields are optional, and not included in the SOAP request in this code example. 
    Please replace with appropriate parameters of the SOAP call and variables. 
"""
def ProcessPayments(idap, amount, refcode, groupTitle = None):
    
    # Sandbox URL for the API function
    url = payer_url
    #Production URL for the API function
    #url="https://api.tipalti.com/v11/PayerFunctions.asmx"
    
    #Payload = SOAP request
    payload = """<x:Envelope
	xmlns:x=\"http://schemas.xmlsoap.org/soap/envelope/\"
	xmlns:tip=\"http://Tipalti.org/\">
	<x:Header/>
	<x:Body>
		<tip:ProcessPayments>        
			<tip:payerName>{req_payername}</tip:payerName>         
			<!-- <paymentGroupTitle>{req_groupTitle}</paymentGroupTitle> -->         
			<tip:tipaltiPaymentsOrders>              
				<tip:TipaltiPaymentOrderItem>                  
					<tip:Idap>{req_idap}</tip:Idap>                
					<tip:Amount>{req_amount}</tip:Amount>                  
					<tip:RefCode>{req_refcode}</tip:RefCode>              
				</tip:TipaltiPaymentOrderItem>         
			</tip:tipaltiPaymentsOrders>          
			<tip:timeStamp>{req_time}</tip:timeStamp>          
			<tip:key>{req_key}</tip:key>      
		</tip:ProcessPayments>   
	</x:Body>
</x:Envelope>"""
    headers = {
      'Content-Type': 'text/xml; charset=utf-8',
      'SOAPAction': 'http://Tipalti.org/ProcessPayments'
    }
    #Get the timestamp
    now = str(math.floor(time.time()))
    
    #Generate the authentication string, for this API call & UTF-8 encode.
    """
    Replace the variables if the authentication string is different. 
    EAT Parameters were not considered in this function. 
    
    If Group Title has a value, 
    auth_str = PayerName+idap+now+groupTitle
    """
    auth_str = PayerName+now
    auth_str.encode(encoding = 'UTF-8')
    
    #Generate the HMAC256 key, with private key and authentication string. 
    key = hmac.new(api_key.encode(), auth_str.encode(), hashlib.sha256).hexdigest()
    
    # Print key to verify if it is correct. 
    #print(key)
    
    #Send the request, save the response. The data sent for the request is mentioned here.
    response = requests.request("POST", url, headers=headers, data=payload.format(req_payername=PayerName, req_idap = idap, req_key=key,req_time=now, req_amount=amount, req_refcode=refcode,req_groupTitle=groupTitle))
    
    #Pretty Print for Aesthetic reasons
    prettyprint.prettyXML(response.text)
    
####################################################################################################################################
"""CreateOrUpdateInvoices
    Sample function to create Invoice with minimal details. 
    Date format : YYYY-MM-DD
    Currency of the invoice is used in the lines. Create <InvoiceLine> for more lines.
    AP account can be left blank.
    Based on workflow, change invoice status/include GL accounts/Purchase Orders/Item Receipts
    GL accounts/Purchase Order/Item Receipts not covered.
    Refer to documentation for additional info
    https://support.tipalti.com/Content/Topics/Development/APIs/PayerAPI/InvoicesAndBills/CreateOrUpdateInvoices/Intro.htm
    """

def CreateOrUpdateInvoices(idap, bill_ref, inv_date, due_date, inv_entity, inv_number, currency, line1_amount, line1_desc, inv_desc=None, inv_sub=None, ap_acc=None, ap_acc_id=None, approve="false",paid_manual="false", inv_status=None, approver1_name=None, approver1_email=None):
    
    url = payer_url
    
    #Payload - SOAP Request with Invoice Lines. 
    payload = """<x:Envelope
    xmlns:x="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:tip="http://Tipalti.org/">
    <x:Header/>
    <x:Body>
        <tip:CreateOrUpdateInvoices>
            <tip:payerName>{req_payername}</tip:payerName>
            <tip:timestamp>{req_time}</tip:timestamp>
            <tip:key>{req_key}</tip:key>
            <tip:invoices>
                <tip:TipaltiInvoiceItemRequest>
                    <tip:Idap>{req_idap}</tip:Idap>
                    <tip:InvoiceRefCode>{req_bill_ref}</tip:InvoiceRefCode>
                    <tip:InvoiceDate>{req_inv_date}</tip:InvoiceDate>
                    <tip:InvoiceDueDate>{req_due_date}</tip:InvoiceDueDate>
                    <tip:InvoiceLines>
                        <tip:InvoiceLine>
                                <tip:Currency>{req_currency}</tip:Currency>
                                <tip:Amount>{req_line1_amount}</tip:Amount>
                                <tip:Description>{req_line1_desc}</tip:Description>
                        </tip:InvoiceLine>
                    </tip:InvoiceLines>
                    <tip:Description>{req_inv_desc}</tip:Description>
                    <tip:CanApprove>{req_approve}</tip:CanApprove>
                    <tip:InvoiceInternalNotes></tip:InvoiceInternalNotes>
                    <tip:IsPaidManually>{req_paid_manual}</tip:IsPaidManually>
                    <tip:IncomeType></tip:IncomeType>
                    <tip:InvoiceStatus>{req_inv_status}</tip:InvoiceStatus>
                    <tip:Currency>{req_currency}</tip:Currency>
                    <tip:Approvers>
                        <tip:TipaltiInvoiceApprover>
                            <tip:Name>{req_approver1_name}</tip:Name>
                            <tip:Email>{req_approver1_email}</tip:Email>
                            <tip:Order>1</tip:Order>
                        </tip:TipaltiInvoiceApprover>
                    </tip:Approvers>
                    <tip:InvoiceNumber>{req_inv_number}</tip:InvoiceNumber>
                    <tip:PayerEntityName>{req_inv_entity}</tip:PayerEntityName>
                    <tip:InvoiceSubject>{req_inv_sub}</tip:InvoiceSubject>
                    <tip:ApAccountNumber>{req_ap_acc}</tip:ApAccountNumber>
                    <tip:ApAccountExternalId>{req_ap_acc_id}</tip:ApAccountExternalId>
                </tip:TipaltiInvoiceItemRequest>
            </tip:invoices>
        </tip:CreateOrUpdateInvoices>
    </x:Body>
</x:Envelope>
    """
    headers = {
      'Content-Type': 'text/xml; charset=utf-8'
    }
    
    #Get the timestamp
    now = str(math.floor(time.time()))
    
    #Generate the authentication string, for this API call & UTF-8 encode.
    auth_str = PayerName+now
    auth_str.encode(encoding = 'UTF-8')
    
    #Generate the HMAC256 key, with private key and authentication string. 
    key = hmac.new(api_key.encode(), auth_str.encode(), hashlib.sha256).hexdigest()
    
    # Print key to verify if it is correct. 
    #print(key)
    
    #Send the request, save the response. The data sent for the request is mentioned here.
    response = requests.request("POST", url, headers=headers, 
                                data=payload.format(req_payername=PayerName, req_idap=idap, req_key=key, 
                                                              req_time=now, req_bill_ref=bill_ref, req_inv_date=inv_date, 
                                                              req_due_date=due_date, req_inv_entity=inv_entity, req_inv_number=inv_number, 
                                                              req_currency=currency, req_line1_amount= line1_amount, req_line1_desc=line1_desc,
                                                              req_inv_desc=inv_desc,
                                                              req_inv_sub=inv_sub, req_ap_acc=ap_acc, req_ap_acc_id=ap_acc_id,
                                                              req_approve=approve, req_paid_manual=paid_manual, req_inv_status=inv_status,
                                                              req_approver1_name=approver1_name, req_approver1_email=approver1_email))

    #Pretty Print for Aesthetic reasons
    prettyprint.prettyXML(response.text)


####################################################################################################################################

                                