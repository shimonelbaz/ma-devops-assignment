# ma-devops-assignment
MoonActive's Home Assignment for DevOps Engineer Position


## Description
This project will 

The workflows takes a few assumptions and corresponding desicions:
1. The workflow will be triggred only manually 
2. The version needs to be build at every execution of the workflow (meaning the versions is always bumped and there is no point in saving previous values)
3. All webapps will be deployed to the same namespace: webapp)

### Prerequisites
This code assumes that you have an available Kubernetes cluster with the following prerequiesites :
1. Accessible Nginx Ingress endpoint (if needed, basic yaml can be found under cluster-prerequisites folder)
2. Kcert operator installed for SSL management (if needed, basic yaml can be found under cluster-prerequisites folder)
3. KubeConfig should be available as a github secret

### Instructions