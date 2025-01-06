import requests
import argparse
import sys
import xml.dom.minidom

def send_soap_request(url, envelope, soap_action):
    """
    Sends a SOAP request with the provided envelope and action.

    :param url: Target SOAP service URL
    :param envelope: Full SOAP XML envelope as a string
    :param soap_action: SOAPAction header value
    """
    try:
        response = requests.post(
            url,
            data=envelope,
            headers={"SOAPAction": soap_action, "Content-Type": "text/xml; charset=utf-8"}
        )

        # Parse and pretty-print the XML response
        formatted_xml = xml.dom.minidom.parseString(response.content)
        print(formatted_xml.toprettyxml(indent="  "))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Send a SOAP request to a specified URL with a customizable SOAP envelope."
    )
    parser.add_argument(
        "-u", "--url", required=True, help="The target URL of the SOAP service."
    )
    parser.add_argument(
        "-e", "--envelope", required=True, 
        help="Path to the file containing the SOAP envelope (XML format)."
    )
    parser.add_argument(
        "-a", "--action", required=True,
        help="The SOAPAction header value."
    )
    args = parser.parse_args()

    # Read the SOAP envelope from the file
    try:
        with open(args.envelope, 'r') as file:
            envelope = file.read()
    except Exception as e:
        print(f"Error reading the SOAP envelope file: {e}")
        sys.exit(1)

    # Send the SOAP request with the provided envelope and action
    send_soap_request(args.url, envelope, args.action)

if __name__ == "__main__":
    main()
