from client import OrderDeliveryTimelineClient
client = OrderDeliveryTimelineClient()
print(client.get_timeline("10001", "90210"))