Azure Machine Learning Cookiecutter Template
============================================

Setting up a project with Azure Machine Learning can be quite a lot of work
some times. This template helps you set up a standard project layout.

.. contents::

Getting started
---------------
To use the template, follow these steps:

- Open a new terminal window
- Execute the command :code:`cookiecutter https://github.com/wmeints/azureml-cookiecutter`
- Follow the on-screen instructions to set up your project

The project layout
------------------
This template generates the following layout:

.. code::

    ├─── README.md                  # Describes how to operate the project
    ├─── requirements.txt           # Dependencies used by the project
    │
    ├─── my_project
    │    ├─── score.py              # The inference script
    │    └─── train.py              # The training script
    │
    ├─── data                       # Stores the datasets
    ├─── docs                       # Stores the project documentation
    ├─── reports                    # Stores generated reports
    ├─── notebooks                  # Stores Python notebooks
    └─── tasks
         ├─── deploy_model.py       # Deploys the model 
         ├─── make_dataset.py       # Creates the dataset for training
         ├─── make_environment.py   # Creates a compute environment
         ├─── make_workspace.py     # Creates or updates the Azure Machine Learning Workspace
         └─── train_model.py        # Trains the model using on the compute environment

Making changes to the project
----------------------------
If you think that something doesn't work, please open a new issue in this repository.
I appreciate any pull requests that help improve my work. 
