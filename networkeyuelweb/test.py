import os
from dotenv import load_dotenv
from networkeyuelweb import networkeyuelweb
from utils import generate_unique

load_dotenv()

networkeyuelAppID = os.environ.get("NetworkEyuelAppID")
networkeyuelAppKey = os.environ.get("NetworkEyuelAppKey")
networkeyuelShortCode = os.environ.get("NetworkEyuelShortCode")
networkeyuelPublicKey = os.environ.get("NetworkEyuelPublicKey")
receiveName = "Test"

tele = NetworkEyuelWeb(networkeyuelAppID, networkeyuelAppKey, networkeyuelShortCode, networkeyuelPublicKey, receiveName)
subject = "Payment"
totalAmount = 10
nonce = generate_unique([], 32)
outTradeNo = generate_unique([], 32)
notifyUrl = "https://example.com/"
returnUrl = "https://example.com/"

response = tele.send_request(subject, totalAmount, nonce, outTradeNo, notifyUrl, returnUrl)
print(response)
