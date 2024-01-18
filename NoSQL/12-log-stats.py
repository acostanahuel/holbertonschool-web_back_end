#!/usr/bin/env python3
"""task 12"""

if __name__ == '__main__':
    import pymongo

    # MongoDB connection
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    # Count the total number of documents in the collection
    total_logs = collection.count_documents({})

    # Count the number of documents with each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in http_methods:
        method_count = collection.count_documents({"method": method})
        method_counts[method] = method_count

    # Count the number of documents with method=GET and path=/status
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Print the statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")