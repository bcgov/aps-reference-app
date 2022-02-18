# API Programme Services Reference Application

This project is an example of a UI and API integrated with APS Kong API Gateway and Keycloak Identity Provider.

## Deploying in Openshift

### Build and Push Packages to Artifactory

Reference: https://github.com/BCDevOps/developer-experience/blob/master/apps/artifactory/DEVHUB-README.md

```
export REPO_NAME="a264-docker"

docker login -u <USER_NAME> -p <USER_PASSWORD> artifacts.developer.gov.bc.ca/${REPO_NAME}

cd microservices/hello-py-api

docker build --tag artifacts.developer.gov.bc.ca/${REPO_NAME}/hello-py-api .

docker push artifacts.developer.gov.bc.ca/${REPO_NAME}/hello-py-api:latest
```

### Permit Pulling from Artifactory

```
kubectl create secret docker-registry artifactory-pull \
    --docker-server=artifacts.developer.gov.bc.ca \
    --docker-username=<username> \
    --docker-password=<password> \
    --docker-email=<username>@<namespace>.local
```

### Deploy UI and API with Helm

```
helm dependency update ./chart
helm upgrade --install aps-ref ./chart
```

## Development

### Microservices

**hello-py-api** followed the `FastAPI` Tutorial: https://fastapi.tiangolo.com/tutorial/first-steps/

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
