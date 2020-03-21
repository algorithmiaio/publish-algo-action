# publish-algo-action
Publishes a secessfully built and published algorithm to www.algorithmia.com

Returns true if publish was successful, returns with an Exception if something went wrong.

# Action Input

```
inputs:
  mgmt_api_key:
    description: 'your Algorithmia Management API key'
    required: true
  api_address:
    description: 'The API address for the Algorithmia Cluster you wish to connect to'
    required: false
    default: 'https://api.algorithmia.com'
  algorithm_name:
    description: 'The name of this Algorithm on Algorithmia'
    required: true
  version_schema:
    description: 'identifier to describe how to promote this release'
    required: false
    default: "minor"
```

 ```
    mgmt_api_key - (required) - your Algorithmia Management API key, which you can learn about [here](https://algorithmia.com/developers/algorithm-development/algorithm-management).
    api_address - (optional) - The Algorithmia API cluster address you wish to connect to, if using a private cluster; please provide the correct path to your environment.
    algorithm_name (required) - The algorithmia algorithm name for project you're publishing. This algorithm name must refer to the github repository you attach this action to in order to work properly.
    version_schema - (optional) - The [semantic version]() parameter that will get incremented whenever this action gets triggered. May be "Major", "Minor", or "Revision"
```


# Example

```
name: Algorithmia publish-algo

on:
  release

jobs:
  publish-algo:
    - name: Algorithmia publish-algo
      uses: algorithmiaio/publish-algo-action@v0.1.0-rc2
      with:
        mgmt_api_key: {{ secrets.ALGO_MGMT_KEY }}
	api_address: {{ screts.ALGORITHMIA_API_ADDRESS }}
        algorithm_name: zeryx/algorithmia_ci
        version_schema: revision
```
