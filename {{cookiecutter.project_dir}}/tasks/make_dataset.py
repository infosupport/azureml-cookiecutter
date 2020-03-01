"""
Make dataset
=============
This task helps to create a new dataset in the workspace. 
It uploads files to the datastore and then registers the dataset.

Please note, files are uploaded to the folder you specify.
If that folder already contains data, it's automatically overwritten!

We're assuming you're uploading CSV files for the moment.
If you've got other data, modify this task accordingly.

Parameters
-----------
- name: The name of the dataset
- input_folder: The path to the folder that contains the data to upload
- output_folder: The path inside the datastore where the data should be stored
"""

import click
from azureml.core import Workspace, Dataset

@click.command()
@click.option('--name', help='The name of the dataset')
@click.option('--input_folder', help='The folder containing the dataset files')
@click.option('--output_folder', help='The folder in the datastore where the dataset should be stored')
def main(name, input_folder, output_folder):
    ws = Workspace.from_config()
    datastore = ws.get_default_datastore()
    
    datastore.upload(input_folder, output_folder, show_progress=True, overwrite=True)

    try:
        Dataset.get_by_name(ws, name)
        create_new_version=True
    except:
        create_new_version=True
        
    ds = Dataset.Tabular.from_delimited_files([(datastore, output_folder)])
    ds.register(ws, name, create_new_version=create_new_version)

if __name__ == '__main__':
    main()