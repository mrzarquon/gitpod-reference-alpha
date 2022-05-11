## Basic EKSCTL driven example

Using the provided gitpod-cluster.yml and eksctl, you can provision a basic EKS cluster with the baseline dependencies for a self contained installation. This does not use any external dependencies at the moment, so should be considered a throw away environment. 

If you do use ACME certificates and Route53, it will require additional steps for DNS configuration outside the scope of this document.

The eksctl configuration file is [here](multizone.yml), updating the region, name, and tags accordingly at top should be sufficient.

This document assume's you have installed:
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html)
- [cert-manager kubectl plugin](https://cert-manager.io/docs/installation/kubectl-plugin/)
- [aws cli version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


The steps are:
- Provision EKS Cluster without nodegroups
- Remove AWS Networking and replace with Calico CNI for higher pod capacity
- Provision EKS Cluster's nodegroups
- Install certificate manager, with adjustments provided to work with Calico in EKS
- Run Replicated installation procession for Gitpod


### Create Cluster
`eksctl create cluster --config-file multizone.yml --without-nodegroup`

update kubeconfig : `aws eks update-kubeconfig --name lab`

### Install Calico
To ensure the cluster is deployed only so you can then install calico
```bash
# remove existing aws setup and install calico
kubectl delete ds aws-node -n kube-system
kubectl apply -f https://docs.projectcalico.org/manifests/calico-vxlan.yaml
```

### Create node groups
```
eksctl create nodegroup --config-file multizone.yml --include workspace
```

### Install Cert-manager
install cert-manager, with hostport:true, fsGroup:1001
```
kubectl cert-manager x install --namespace cert-manager --set installCRDs=true \
    --set webhook.hostNetwork=true --set serviceAccount.name='cert-manager' --set serviceAccount.create='false' \
    --set webhook.securePort=10260
```
Edit deployment for fsGroup setting

### Install kots (Replicated) and Gitpod
```
curl https://kots.io/install | bash
kubectl kots install gitpod -n gitpod
```
