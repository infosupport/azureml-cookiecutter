"""
Make workspace
===============
This task creates a new workspace for your project if none exists yet.
It then writes the configuration to disk so you can run tasks in the project.

Please note, if the workspace already exists, this script will only write the
configuration to the root folder of the project.

Parameters
----------
- name: The name of the workspace 
- resource_group: The name of the resource group in which to create the workspace
- location: The data center location to deploy to
- subscription_id: The GUID of the subscription to deploy to

You can find the subscription ID using the Azure CLI :code:`az account list` or
by going to https://portal.azure.com/ and looking it up in your subscriptions list.
"""

import click
from azureml.core import Workspace

@click.command()
@click.option('--name', help='The name of the workspace to create or manage')
@click.option('--resource_group', help='The name of the resource group')
@click.option('--location', help='The data center location to deploy to')
@click.option('--subscription_id', help='GUID identifying the subscription you want to deploy to')
def main(name, resource_group, location, subscription_id):
    ws = Workspace.create(
        name=name, 
        resource_group=resource_group, 
        subscription_id=subscription_id,
        location=location,
        exist_ok=True, 
        show_output=True)

    ws.write_config()

if __name__ == '__main__':
    main()