import sys
import string
import subprocess
import win32com
import win32api
import wmi

def URLStrip(DLPVariable):
    import tldextract
    if 'recipient-url1=' in DLPVariable:
        stripped_URL = (DLPVariable.replace('recipient-url1',""))
        if stripped_URL != 'Unknown':
            URL_obj = tldextract.extract(stripped_URL)
            print('URL{}'.format(URL_obj.registered_domain))


if __name__ == '__main__':
    """Options"""

    URLStrippingScript= "ON"

    InboundAttributes = sys.argv[1:]
    InboundValue = str(sys.argv[1:])
    for DLPVariable in InboundAttributes:
        if URLStrippingScript == "ON":
            URLStrip(DLPVariable)

    exit(0)
