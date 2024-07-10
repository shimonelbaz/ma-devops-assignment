# ma-devops-assignment
MoonActive's Home Assignment for DevOps Engineer Position


## Description
This project will demonstrate the abilty to build, deploy and run multiple services in the same namespace which generates api call to external services and return a raw or parsed response. 

The workflows takes a few assumptions and corresponding desicions:
1. The workflow will be triggred only manually 
2. The version needs to be build at every execution of the workflow (meaning the versions is always bumped and there is no point in saving previous values)
3. All webapps will be deployed to the same namespace: webapp
4. No need to expose the openAPI interactive documentation page
---

### Prerequisites
This code assumes that you have an available Kubernetes cluster with the following prerequiesites :
1. Accessible Nginx Ingress endpoint (if needed, basic yaml can be found under cluster-prerequisites folder)
2. Kcert operator installed for SSL management (if needed, basic yaml can be found under cluster-prerequisites folder)
3. KubeConfig should be available as a github secret
4. webapp namespace shuold exist in advance 
---

### Instructions
#### Deployment
In order to deploy a version, go to the [Actions Page](https://github.com/shimonelbaz/ma-devops-assignment/actions/workflows/build.yaml) and run the action. 

choose the service you wish to deploy from the droplist.

#### Usage
Once the deployment id done, the services can be used in the following ways:
1. Readiness check - Browse to: https://excercise.elbaz.io/{service-name}/ready . This should return a 200 code if the service is ready.
2. Getting a random fact / joke - Browse to: https://excercise.elbaz.io/{service-name} .This will return a random fact / joke.
3. Getting the raw response of the requests - Browse to: https://excercise.elbaz.io/{service-name}?raw=true . This will return the raw data returned from the api server
4. Using cURL - curl {same-urls-as-above}

#### Adding a New Service
Adding a new service is simple:
1. Edit the workflow file - .github/workflows/build.yaml
2. Add the service name to the inputs list of the workflow
3. Add the service information [name, URL, port (choose any free one)] to the SERVICE_PARAMETERS json 
4. Note, if the response from the API is not a json or that the requested value is not in the fields called - text, value - it needs to be added to the python code, otherwise the response will always be the raw one.