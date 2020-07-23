from django.db import models
from django.contrib.auth.models import User
import xml.etree.ElementTree as ET
from zeep import Client, Settings
from zeep.exceptions import Fault, TransportError, XMLSyntaxError

# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length = 100, unique=True)
    rate_increase = models.DecimalField(decimal_places=2, max_digits=2)
    def __str__(self):
        return self.company_name
    

class Shipment(models.Model):
    user_name = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    tracking_number = models.IntegerField()
    total_price = models.FloatField()
    shipment_date = models.DateTimeField()    
    company_name = models.ForeignKey(Company, to_field="user", on_delete=models.CASCADE, related_name="companyname")
    service_level = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    ref_1 = models.CharField(max_length=20)
    ref_2 = models.CharField(max_length=20)
    weight = models.IntegerField()
    def __str__(self):
        return str(self.company_name) + ": " + str(self.tracking_number)   
    def ship():
        # Set Connection
        settings = Settings(strict=False, xml_huge_tree=True)
        client = Client('SCHEMA-WSDLs/Ship.wsdl', settings=settings)

# Set SOAP Headers
        headers = {

            'UPSSecurity': {
                'UsernameToken': {
                    'Username': 'krogfammgmt',
                    'Password': 'Valorem@1234'
                 },

                'ServiceAccessToken': {
                    'AccessLicenseNumber': '9D8407BE6DCC79D5'
                 }

            }
        }

# Create request dictionary
        requestDictionary = {

            "RequestOption": "nonvalidate",
            "TransactionReference": {
                "CustomerContext": "Customer Context"
            }
        }

# Create Ship request dictionary
        shipmentRequestDictionary = {

            "Description": "Ship WS test",
            "Package": {
                "Description": '',
                "Dimensions": {
                    "Height": "2",
                    "Length": "7",
                    "UnitOfMeasurement": {
                        "Code": "IN",
                        "Description": "Inches"
                    },
                    "Width": "5"
                },
                "PackageWeight": {
                    "UnitOfMeasurement": {
                        "Code": "LBS",
                        "Description": "Pounds"
                    },
                    "Weight": "10"
                },
                "Packaging": {
                    "Code": "02",
                    "Description": ""
                }
            },
            "PaymentInformation": {
                "ShipmentCharge": {
                    "BillShipper": {
                        "AccountNumber": "81r651"
                    },
                    "Type": "01"
                }
            },
            "Service": {
                "Code": "03",
                "Description": ""
            },
            "ShipFrom": {
                "Address": {
                    "AddressLine": "Street name",
                    "City": "City Name",
                    "CountryCode": "US",
                    "PostalCode": "Postal Code",
                    "StateProvinceCode": "Sate Code"
                },
                "AttentionName": "",
                "FaxNumber": "1234567890",
                "Name": "",
                "Phone": {
                    "Number": "1234567890"
                }
            },
            "ShipTo": {
                "Address": {
                    "AddressLine": "Street Name",
                    "City": "City Name",
                    "CountryCode": "US ",
                    "PostalCode": "Postal Code",
                    "StateProvinceCode": "State or province Code"
                },
                "AttentionName": "Valorem",
                "Name": "Valorem",
                "Phone": {
                    "Number": "123456789"
                }
            },
            "Shipper": {
                "Address": {
                    "AddressLine": "Street Name",
                    "City": "City Name",
                    "CountryCode": "US",
                    "PostalCode": "Postal Code",
                    "StateProvinceCode": "State or Province Code"
                },
                "AttentionName": "",
                "FaxNumber": "123456789",
                "Name": "ShipperName",
                "Phone": {
                    "Extension": "1",
                    "Number": "123456789"
                },
                "ShipperNumber": "Shipper Number",
                "TaxIdentificationNumber": "123456"
            }

        }

# Create label specification dictionary
        labelSepcificationDictionary = {

            "HTTPUserAgent": "Mozilla/4.5",
            "LabelImageFormat": {
                "Code": "GIF",
                "Description": "GIF"
            }

        }

# Try operation
        try:
            response = client.service.ProcessShipment(_soapheaders=headers, Request=requestDictionary,
                                              Shipment=shipmentRequestDictionary,
                                              LabelSpecification=labelSepcificationDictionary)
            print(response)


        except Fault as error:
            print(ET.tostring(error.detail))


    
    

