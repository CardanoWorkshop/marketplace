# Broker settings
broker_url = "amqp://guest:guest@nft-market-rabbit:5672//"

# List of modules to import when the Celery worker starts
imports = ("nft_market.api.tasks",)