# action-prefect-flow-trigger
Triggers prefect flows in the Prefect cloud

## inputs
```shell
name: deployment_name
description: "prefect cloud deployment name"
required: true

name: workspace_name
description: "Prefect cloud workspace name"
required: true

name: api_key
description: "Prefect cloud api key, please provide a secret"
required: true
```