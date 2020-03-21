#!/usr/bin/python

import Algorithmia
import os

if __name__ == "__main__":
    api_key = os.getenv("INPUT_API_KEY")
    api_address = os.getenv("INPUT_API_ADDRESS")
    algo_name = os.getenv("INPUT_ALGORITHM_NAME")
    algo_schema = os.getenv("INPUT_VERSION_SCHEMA")

    algo_hash = os.getenv("GITHUB_SHA")

    client = Algorithmia.client(api_key=api_key, api_address=api_address)

    algo = client.algo("{}/{}".format(algo_name, algo_hash))
    info = algo.versions(1).results[0]['version_info']

    if "version_type" in info:
        cur_version = info['version_type']
        print("--- last release version : {} ---".format(cur_version))
    else:
        cur_version = None
        print("--- working with fresh project (no previous release found)")

    if algo_schema not in ["major", "minor", "revision"]:
        raise Exception("{} is not considered a valid algorithm version schema".format(algo_schema))
    print("--- releasing new {}".format(algo_schema))
    algo.publish(version_info={"version_type": algo_schema, "release_notes": "automatically deployed by CI"})
    latest_version = algo.versions(1).results[0]['version_info']
    print("--- new version {} successfully published".format(latest_version))


