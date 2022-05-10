from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda, EC2AutoScaling, EC2Instance, EC2ContainerRegistryRegistry, ElasticContainerServiceContainer
from diagrams.aws.database import RDSMysqlInstance
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.network import ELB
from diagrams.onprem.client import User


with Diagram("AWS Single Region Multizone", show=False):
    source = User("developer")
    
    lb = ELB("LoadBalancer")

    with Cluster("EKS Cluster"):
        with Cluster("Services Nodegroup"):
            services = ECS('Proxy')
            

        with Cluster("Workspaces Nodegroups"):
            with Cluster("headless and services"):
                background = [
                    EC2Instance("c6i.2xlarge"),
                    ECS('ws-daemon'),
                    ECS('image-builder')
                ]
            with Cluster("regular"):
                runtime = [
                    EC2Instance("m6i.4xlarge"),
                    ECS("Dev Workspace")
                ]


    registry = EC2ContainerRegistryRegistry("Workspace Storage")
    object_storage = S3("Runtime Storage")
    database = RDSMysqlInstance("Gitpod DB Storage")

    runtime << object_storage
    services << database

    source >> lb >> services \
        >> background \
        >> registry \
        >> runtime

    source >> lb >> services >> runtime
