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