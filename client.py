class OrderDeliveryTimelineClient:
    def get_timeline(self, origin_zip: str, dest_zip: str) -> dict:
        return {"days": 3}