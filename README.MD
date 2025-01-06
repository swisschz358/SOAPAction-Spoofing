# SOAPAction-Spoofing Script

This script is designed to test SOAPAction spoofing vulnerabilities in SOAP-based web services. It allows users to specify a target URL and a SOAP envelope payload, providing a flexible way to assess potential vulnerabilities.

## Features
- Accepts custom SOAP envelopes for various SOAP web services.
- Allows dynamic specification of the target URL and SOAPAction header.
- Pretty-prints XML responses for readability.
- Universally adaptable to different SOAP service implementations.

## Prerequisites
Ensure you have Python installed along with the required libraries. Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

### Command-line Arguments
- `-u` / `--url`: Specifies the target URL of the SOAP service (required).
- `-e` / `--envelope`: Path to the file containing the SOAP envelope (required).
- `-a` / `--action`: Specifies the SOAPAction header value (required).

### Example
1. Create a SOAP envelope file (e.g., `soap_request.xml`):
   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
       <soap:Body>
           <ExecuteCommand>
               <param>example</param>
           </ExecuteCommand>
       </soap:Body>
   </soap:Envelope>
   ```

2. Run the script:
   ```bash
   python script.py -u http://<TARGET-IP>:3002/wsdl -e soap_request.xml -a "ExecuteCommand"
   ```

3. Example Output:
   ```xml
   <?xml version="1.0" ?>
   <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
       <soap:Body>
           <ExecuteCommandResponse>
               <result>Success</result>
           </ExecuteCommandResponse>
       </soap:Body>
   </soap:Envelope>
   ```

## Notes
- Ensure you have the appropriate permissions to assess the target system.
- Always perform testing responsibly and within the bounds of legal agreements.

## License
This script is licensed under the MIT License. See the LICENSE file for more details.
