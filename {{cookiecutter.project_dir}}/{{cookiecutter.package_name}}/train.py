import joblib
from azureml.core import Run

# The run is automatically determined.
# Use this to log data, get access to dataset, and publish your model.
run = Run.get_context()

# STEP 1: Get the datasets
################################################################################
# Datasets are made available in the input_datasets dictionary.

ds1 = run.input_datasets['ds1']

# Option 1: Mount the dataset
# import tempfile

# mount_point = tempfile.mkdtemp()
# mount_context = ds1.mount(mount_point)
# mount_context.start()

# Option 2: Convert the dataset to a pandas dataframe
# df = ds.to_pandas_dataframe()

# STEP 2: Preprocess the dataset
################################################################################
# Perform some last-minute transformations before training the model here.


# STEP 3: Train the model
################################################################################
# Train your model here. Please note, we're assuming scikit-learn in the 
# train_model task. If you plan to use Tensorflow, be sure to change the 
# estimator in the task as well. You can find more information here:
# https://docs.microsoft.com/en-us/azure/machine-learning/how-to-train-ml-models
# 
# Use run.log(), run.log_image(), run.log_table()
# or run.log_row() to log metrics as part of the run.
# You can learn more about logging here:
# https://docs.microsoft.com/en-us/azure/machine-learning/how-to-track-experiments


# STEP 4: Register the model
################################################################################
# First, store the model on disk by using joblib.dump('outputs/model.bin')
# then, call run.upload_file('model.bin', 'outputs/model.bin')
# after that, call run.register_model('model_name', 'model.bin')

# joblib.dump(model, 'outputs/model.bin')
# run.upload_file('model.bin', 'outputs/model.bin')
# run.register_model('model_name', 'model.bin')
