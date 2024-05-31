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

name: params:
description: "Prefect flow parameters (optional)"
required: false
default: ''
```

## Example

```yaml
jobs:
  trigger_mario_e2e:
    if: github.ref == 'refs/heads/master'
    runs-on: ubuntu-latest
    steps:
      - name: trigger-prefect-flow
        uses: landtechnologies/action-prefect-flow-trigger@v1.0.0
        with:
          deployment_name: data_ingested_test/prod
          workspace_name: "dataopslandtech/landtech"
          api_key: ${{secrets.PREFECT2_API_KEY}}
```