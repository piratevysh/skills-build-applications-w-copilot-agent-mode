"""Verify data in octofit_db using pymongo."""
import os
from pymongo import MongoClient

def verify():
    client = MongoClient("mongodb://localhost:27017")
    db = client.get_database("octofit_db")
    collections = ["octofit_tracker_userprofile", "octofit_tracker_team", "octofit_tracker_activity"]
    results = {}
    for c in collections:
        if c in db.list_collection_names():
            results[c] = db[c].count_documents({})
        else:
            results[c] = 0
    for k, v in results.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    verify()
