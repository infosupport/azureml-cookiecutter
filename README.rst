Azure Machine Learning Cookiecutter Template
============================================

Setting up a project with Azure Machine Learning can be quite a lot of work
some times. This template helps you set up a standardized project layout.

.. contents:: In this README we'll cover the following topics:

System requirements
-------------------
- Python 3.8.6 or higher
- Cookiecutter

Why this template?
------------------
We ran into the same issues over and over again with our machine learning projects.
We do like creativity, but we think that it's good to have a solid base to start from.
It saves you and your team a lot of time, because you don't have to spend time discussing the project 
layout and MLOps frameworks you're going to use.
All we ask is that you pick the machine learning framework and data processing tool.
The rest is all taken care of. You're welcome :-)

Getting started
---------------
To use the template, follow these steps:

- Open a new terminal window
- Execute the command :code:`pip install cookiecutter`
- Execute the command :code:`cookiecutter https://github.com/infosupport/azureml-cookiecutter`
- Follow the on-screen instructions to set up your project

The project layout
------------------
This template generates the following layout:

.. code::

    ├─── README.md                  # Describes how to operate the project
    ├─── requirements.txt           # Dependencies used by the project
    ├─── .gitignore                 # Ignored files for GIT
    ├─── .amlignore                 # Ignored files for the Azure ML workspace
    ├─── setup.py                   # Setup file in case you want to package your project as a pip package.
    ├─── MANIFEST.in                # Manifest file for pip packaging.
    │
    ├─── my_project
    │    ├─── score.py              # The inference script
    │    └─── train.py              # The training script
    │
    ├─── data                       # Stores the datasets
    ├─── docs                       # Stores the project documentation
    ├─── reports                    # Stores generated reports
    ├─── notebooks                  # Stores Python notebooks
    ├─── tests                      # Stores the unit-tests for the project
    └─── tasks
         ├─── deploy_model.py       # Deploys the model 
         ├─── make_dataset.py       # Creates the dataset for training
         ├─── make_environment.py   # Creates a compute environment
         ├─── make_workspace.py     # Creates or updates the Azure Machine Learning Workspace
         └─── train_model.py        # Trains the model using on the compute environment
         
What tools can you use with this project?
-----------------------------------------
We don't prescribe any fixed number of machine learning tools to use with this template.
Azure Machine Learning and this template support a number of machine learning tools:

* Scikit-learn
* Tensorflow
* PyTorch

Aside from these tools, we have tested the template with the following data science libraries:

* Scipy
* Numpy
* Pandas

Can't find the tool you're using? Please let us know if it works for you and we'll add it to this list.

Making changes to the project
----------------------------
If you think that something doesn't work, please open a new issue in this repository.
