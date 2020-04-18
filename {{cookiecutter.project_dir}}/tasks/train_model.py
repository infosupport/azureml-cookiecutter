"""
Train model
===========
This task queues the training script on the remote compute target.
Please, make sure you have a remote environment setup before running this task.

The task assumes that you're using scikit-learn as your machine learning 
framework. Please change the estimator to a matching one, based on what 
you're using. You can find more information about this here:
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-train-ml-models

Parameters
----------
environment : str
    The environment to train the model on
dataset : str
    The input dataset to use for training. (multiple allowed)
experiment : str
    The experiment to use for running the training script
"""

import click
from pathlib import Path
from azureml.core import Workspace, Experiment, Dataset, ComputeTarget
from azureml.train.sklearn import SKLearn


@click.command()
@click.option(
    '--experiment', 
    help='The experiment for which to execute the run'
)
@click.option('--environment', help='The remote environment to use')
@click.option(
    '--dataset', multiple=True, 
    help='The name of the input dataset to use for training'
)
def main(experiment, environment, dataset):
    workspace = Workspace.from_config()
    experiment = Experiment(workspace, experiment)
    compute_target = ComputeTarget(workspace, environment)
    
    # Use the root of the solution as source folder for the run.
    root_folder = Path(__file__).parent.parent

    # Provide each of the datasets to the estimator as a named input.
    # You can acccess these from within the training script.
    datasets = [Dataset.get_by_name(workspace, ds).as_named_input(ds) for ds in dataset]

    estimator = SKLearn(
        source_directory=root_folder,
        entry_script='{{cookiecutter.package_name}}/train.py',
        conda_dependencies_file='conda_dependencies.yml',
        compute_target=compute_target,
        inputs=datasets
    )

    run = experiment.submit(estimator)

    run.wait_for_completion(show_output=True)


if __name__ == "__main__":
    main()