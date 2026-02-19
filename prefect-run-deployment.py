import json
from sys import argv

from prefect.deployments import run_deployment
from prefect.server.schemas.states import StateType

DEPLOYMENT_NAME = argv[1]
# Parameters are merged with the flow defaults
FLOW_PARAMETERS = json.loads(argv[2])

# timeout of 0 means no timeout, the deployment will run and not block execution
timeout=argv[2]

result = run_deployment(name=DEPLOYMENT_NAME, parameters=FLOW_PARAMETERS, timeout=timeout)

# Only check state of run if we're actually waiting for it to complete
if timeout:
    if result.state_type != StateType.COMPLETED:
        raise RuntimeError(result.state.message)