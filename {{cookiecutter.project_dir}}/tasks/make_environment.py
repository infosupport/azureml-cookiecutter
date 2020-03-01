"""
Make compute environment
=========================
This task creates a new compute environment for training your models.
We're assuming that you want at least one node to stay active at all times.
You can change this in the script if you like.

Parameters
-----------
- name: The name of the compute environment
- vm_size: The size of VM to deploy (e.g. Standard_D3_v2 or Standard_NV6)
- nodes: The maximum number of nodes in the cluster.
"""

import click
from azureml.core import Workspace, ComputeTarget
from azureml.core.compute import AmlCompute
from azureml.exceptions import ComputeTargetException


@click.command()
@click.option('--name', help='The name of the compute environment')
@click.option('--vm_size', help='The size of the VM to deploy')
@click.option('--nodes', help='The maximum size of the compute cluster')
def main(name, vm_size, nodes):
    ws = Workspace.from_config()

    try:
        compute_cluster = ComputeTarget(ws, name)
    except:
        compute_config = AmlCompute.provisioning_configuration(
            vm_size=vm_size, min_nodes=1, max_nodes=nodes
        )

        compute_cluster = ComputeTarget.create(ws, name, compute_config)
        compute_cluster.wait_for_completion(show_output=True)

if __name__ == '__main__':
    main()