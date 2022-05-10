# gitpod-reference-alpha

This is a POC repo meant to illustrate how we can generate guide material around different architectures.

It uses python package ["diagrams"](https://diagrams.mingrammer.com/) to render the visual you see below.

## Support

The purpose of these reference architectures are to provide illustrations of how Gitpod can be setup and configured depending on the cloud environment and resource demands.

This content does not come with an SLA but the automations it uses are tested as part of the Gitpod Self Hosted Release testing process, so the settings and design considerations included here in will be vetted.

## Amazon

EKS is the preferred method of running Gitpod in AWS. By using managed nodegroups and the Amazon provided AMIs, there is an option of support through AWS for the infrastructure. 

[AWS Guides](eks/README.md)

