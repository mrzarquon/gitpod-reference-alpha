# gitpod-reference-alpha

EKS Example Cluster
Always provision first with:
`eksctl create cluster --config-file gitpod-cluster.yaml --without-nodegroup`

update kubeconfig : `aws eks update-kubeconfig --name lab`

To ensure the cluster is deployed only so you can then install calico
```bash
# remove existing aws setup and install calico
kubectl delete ds aws-node -n kube-system
kubectl apply -f https://docs.projectcalico.org/manifests/calico-vxlan.yaml

# create node groups
eksctl create nodegroup --config-file gitpod-cluster.yaml --include workspace
```

install cert-manager, with hostport:true, fsGroup:1001
```
kubectl cert-manager x install --namespace cert-manager --set installCRDs=true \
    --set webhook.hostNetwork=true --set serviceAccount.name='cert-manager' --set serviceAccount.create='false' \
    --set webhook.securePort=10260
```

curl https://kots.io/install | bash
kubectl kots install gitpod -n gitpod
