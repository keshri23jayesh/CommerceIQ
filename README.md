# CommerceIQ 

A Basic Curd Opertion in a existing JSON file.

Featares
---

- Build a REST based JSON mock server to easily add, update, delete and access data from a JSON file.
- Every data set should have a parent identifier (entity type), which will be used in the GET APIs.
- Every data set should have an ID (Primary key)
- ID should be immutable, error needs to be thrown if ID is tried to be mutated.
- If you make POST, PUT, PATCH or DELETE requests, changes have to be automatically saved to store.json.
