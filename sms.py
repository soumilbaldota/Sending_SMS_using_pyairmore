from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
import sys

ip=IPv4Address(f'{sys.argv[1]}')
session=AirmoreSession(ip,2333)

print(session.is_server_running )

req_authorization = session.request_authorization()
service = MessagingService(session)
service.send_message(f'+91{sys.argv[2]}',f'{sys.argv[3]}')