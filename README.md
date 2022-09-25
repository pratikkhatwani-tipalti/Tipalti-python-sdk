# Tipalti-python-sdk
Python SDK for Tipalti Payer/Payee Functions for v11 SOAP APIs

## Installation
#
#### For [Python 3.8.8](https://www.python.org/)


## Dependencies

* Python
* [requests](https://pypi.org/project/requests/)
* [bs4](https://pypi.org/project/bs4/)

## Getting Started (configuration.py)
  ```python
  #Private key found on APHUB. Administration -> Apps -> API Key
  PayerName ="YOUR-PAYER-NAME"
  api_key = "YOUR_PRIVATE_APIKEY"

  #Sandbox URLs
  payee_url = "https://api.sandbox.tipalti.com/v11/PayeeFunctions.asmx"
  payer_url = "https://api.sandbox.tipalti.com/v11/PayerFunctions.asmx"

  #Production URLs
  #payee_url = "https://api.tipalti.com/v11/PayeeFunctions.asmx"
  #payer_url = "https://api.tipalti.com/v11/PayerFunctions.asmx"
  ```

## Documentation for API Endpoints

* Payee APIs: https://support.tipalti.com/Content/Topics/Development/APIs/PayeeAPI/Intro.htm
* Payer APIs: https://support.tipalti.com/Content/Topics/Development/APIs/PayerAPI/Intro.htm

### Usage
1. Configure Payer Name and API Key and URL in configuration.py

2. TipaltiRequests.py
    * GetPayeeDetails
    * GetExtendedPayeeDetails
    * UpdateOrCreatePayeeInfo
    * ProcessPayments
    * CreateOrUpdateInvoices

3. GetPayeeDetails, GetExtendedPayeeDetails are complete functions. 
4. UpdateOrCreatePayeeInfo, ProcessPayments, CreateOrUpdateInvoices consist of the basic fields required for usage. 
  
   There is additional documentation on the code to proceed with additions/modifications required to the code UpdateOrCreatePayeeInfo, ProcessPayments, CreateOrUpdateInvoice.

    * UpdateOrCreatePayeeInfo - Only creates the payee with an IDAP. Pass Name/Email/Address/Details accordingly.
    For further documentation refer: https://support.tipalti.com/Content/Topics/Development/APIs/PayeeAPI/UpdatePayee/UpdateOrCreatePayeeInfo/Intro.htm

    * ProcessPayments - Only passes IDAP, Amount, Ref-Code. 
    For further documentation refer: https://support.tipalti.com/Content/Topics/Development/APIs/PayerAPI/PaymentsAndFees/ProcessPayments/Intro.htm

    * CreateOrUpdateInvoices - Only creates invoice with 1 line, add <InvoiceLine> for more. 
    For further documentation refer: https://support.tipalti.com/Content/Topics/Development/APIs/PayerAPI/InvoicesAndBills/CreateOrUpdateInvoices/Intro.htm

5. GetTipaltiPayeeID.py
    * GetTipaltiPayeeID - Returns the Tipalti IDAP of a payee, when the External ID (ERP ID) of a payee is passed. 
      * Uses extractResponse.py to extract the IDAP, and store it in payee_idap
  
  6. extractResponse.py - Used to extract SOAP response values from <tag> value </tag>
    * Can use extractResponse to extarct values for TipaltiRequests and store response in variables
  
  7. sample API calls.py
    * Sample code on how to invoke and call methods from TipaltiRequests.py
  
  8. prettyprint.py
    * Method to format XML response in a clean way for interpretation. Uses BeautifulSoup. 
    * Replace with print if not needed.

The comments in the doc should cover most use cases. 
Please do not hesitate to reach out to pratik.khatwani@tipalti.com for additional questions.

## Common Errors
  * EncryptionKeyValidationFailed - Certain Payee/Payer Functions need EAT parameters, mentioned in the comments in the code. 
  * The payment list cannot be more than 250 items long.
  * CreateOrUpdateInvoices - When using this API function, it is recommended that you don't send more than 200 bills in the request. If you need to create more than 200 bills, please create several requests.
