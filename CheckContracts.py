from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://admin:cosec71@210.28.134.71:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter={
    'tx_count': {
        '$gte': 200, 
        '$lte': 500
    }, 
    'block_number': {
        '$gte': '7000000'
    }
}
sort=list({
    'tx_count': -1
}.items())

result = client['EthereumBigquery']['contracts'].find(
  filter=filter,
  sort=sort
)

for a in result:
    print()
    break