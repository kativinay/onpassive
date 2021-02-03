How to store the data in MongoDB in an array format and get e latest message from the Array list.
    we can create a collection with documents where we can store array values.


query:
    insert array objects into mongo:
    
    db.collection.insertOne(
        {"Users":[{"UserId":101,"UserName":"Vinay"},{"UserId":102,"UserName":"vinaybabu"},
        {"UserId":103,"UserName":"Vinay"},{"UserId":104,"UserName":"vinaybabu"}]}
    );