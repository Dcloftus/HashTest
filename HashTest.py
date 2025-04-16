from Crypto.Hash import BLAKE2b
import json

traitsArray = ["Craftsman","Pragmatic","Curious","Methodical","Driven","Collaborator"]
hashedArray = []

print('Blake 2b Hashing Traits: ' + ' '.join(traitsArray))

for trait in traitsArray:
    h_obj = BLAKE2b.new(digest_bytes=64, key=b'Close-6522407b')
    h_obj.update(str(trait).encode())
    hashedArray.append(h_obj.hexdigest())

print(json.dumps(hashedArray))