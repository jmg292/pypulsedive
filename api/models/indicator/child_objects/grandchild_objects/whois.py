"""
class WhoIs(object):

    FIELD_MAP = {
        "++abuse": "+1.8772376466",
        "++email": "urb6dpdrhxz4@contactprivacy.email",
        "++expires": "2021-11-11 00:00:00",
        "++phone": "+1.8772376466",
        "++privacy": "1",
        "++registered": "2016-11-11 00:00:00",
        "++registrant": "96 Mowat Ave",
        "++registrar": "Google LLC",
        "++updated": "2020-11-12 00:00:00",
        "admin city": "Toronto",
        "admin country": "CA",
        "admin email": "urb6dpdrhxz4@contactprivacy.email",
        "admin name": "Contact Privacy Inc. Customer 124912322",
        "admin organization": "Contact Privacy Inc. Customer 124912322",
        "admin phone": "+1.4165385487",
        "admin postal code": "M4K 3K1",
        "admin state\/province": "ON",
        "admin street": "96 Mowat Ave",
        "creation date": "2016-11-11T21:18:19Z",
        "dnssec": "unsigned",
        "domain name": "pulsedive.com",
        "domain status": "ok https:\/\/www.icann.org\/eppRegistry Registrant ID:",
        "name server": [
            "NS3.DIGITALOCEAN.COM",
            "NS1.DIGITALOCEAN.COM",
            "NS2.DIGITALOCEAN.COM"
        ],
        "please register your domains at": "https:\/\/domains.google.com\/",
        "registrant city": "Toronto",
        "registrant country": "CA",
        "registrant email": "urb6dpdrhxz4@contactprivacy.email",
        "registrant name": "Contact Privacy Inc. Customer 124912322",
        "registrant organization": "Contact Privacy Inc. Customer 124912322",
        "registrant phone": "+1.4165385487",
        "registrant postal code": "M4K 3K1",
        "registrant state\/province": "ON",
        "registrant street": "96 Mowat Ave",
        "registrar": "Google LLC",
        "registrar abuse contact email": "registrar-abuse@google.com",
        "registrar abuse contact phone": "+1.8772376466",
        "registrar iana id": "895",
        "registrar registration expiration date": "2021-11-11T21:18:19Z",
        "registrar url": "https:\/\/domains.google.com",
        "registrar whois server": "whois.google.com",
        "registry domain id": "2073459391_DOMAIN_COM-VRSN",
        "tech city": "Toronto",
        "tech country": "CA",
        "tech email": "urb6dpdrhxz4@contactprivacy.email",
        "tech name": "Contact Privacy Inc. Customer 124912322",
        "tech organization": "Contact Privacy Inc. Customer 124912322",
        "tech phone": "+1.4165385487",
        "tech postal code": "M4K 3K1",
        "tech state\/province": "ON",
        "tech street": "96 Mowat Ave",
        "updated date": "2020-11-12T03:14:58Z",
        "url of the icann whois data problem reporting system": "http:\/\/wdprs.internic.net\/"
    }

    def __init__(self):


    @staticmethod
    def from_dictionary(whois_dict: dict):
        whois = WhoIs()
        field_map = getattr(whois.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in whois_dict:
                setattr(whois, field_map[key_name], whois_dict[key_name])
        return whois
        """