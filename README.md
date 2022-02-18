# API Programme Services Reference Application

[![Lifecycle:Maturing](https://img.shields.io/badge/Lifecycle-Maturing-007EC6?style=for-the-badge)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)
![GitHub](https://img.shields.io/github/license/bcgov/aps-reference-app?style=for-the-badge)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/bcgov/aps-reference-app?label=release&style=for-the-badge)

This project is an example of a UI and API integrated with APS Kong API Gateway and Keycloak Identity Provider.

## Deploying to Openshift

### Pre-requisites for building and packaging the Containers

#### Build and Push Packages to Artifactory

Reference: https://github.com/BCDevOps/developer-experience/blob/master/apps/artifactory/DEVHUB-README.md

```
export REPO_NAME=""

docker login -u <USER_NAME> -p <USER_PASSWORD> artifacts.developer.gov.bc.ca/${REPO_NAME}
```

**Microservices:**

```
cd microservices/hello-py-api

docker build --tag artifacts.developer.gov.bc.ca/${REPO_NAME}/hello-py-api .
docker push artifacts.developer.gov.bc.ca/${REPO_NAME}/hello-py-api
```

**UI:**

```
cd ui/aps-ref-ui

docker build --tag artifacts.developer.gov.bc.ca/${REPO_NAME}/aps-ref-ui:latest .
docker push artifacts.developer.gov.bc.ca/${REPO_NAME}/aps-ref-ui
```

#### Allow Pulling from Artifactory

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

### API Gateway Setup

## Development

### Microservices

**hello-py-api** follows the `FastAPI` Tutorial: https://fastapi.tiangolo.com/tutorial/first-steps/

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### UI

**hello-ui** uses `NextJS` and built running `npx create-next-app aps-ref-ui`

```
npm run dev
```
