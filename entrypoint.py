#!/usr/bin/python

import Algorithmia
import os

if __name__ == "__main__":
    api_key = os.getenv("INPUT_API_KEY")
    api_address = os.getenv("INPUT_API_ADDRESS")
    algo_name = os.getenv("INPUT_ALGORITHM_NAME")
    algo_hash = os.getenv("GITHUB_SHA")
    algo_schema = os.getenv("INPUT_VERSION_SCHEMA")

    client = Algorithmia.client(api_key=api_key, api_address=api_address)

    algo = client.algo("{}/{}".format(algo_name, algo_hash))
    info = algo.versions(1).results[0]['version_info']

    if "version_type" in info:
        cur_version = info['version_type']
        print("--- last release version : {} ---".format(cur_version))
    else:
        cur_version = None
        print("--- working with fresh project (no previous release found)")

    if "*._._" == algo_schema:
        version_type = "major"
    elif "_.*._" == algo_schema:
        version_type = "minor"
    elif "_._.*" == algo_schema:
        version_type = "revision"
    else:
        raise Exception("version schema {} is not an acceptable format".format(algo_schema))
    print("--- releasing new {}".format(version_type))
    algo.publish(version_info={"version_type": version_type, "release_notes": "automatically deployed by CI"})
    latest_version = algo.versions(1).results[0]['version_info']
    print("--- new version {} successfully published".format(latest_version))


