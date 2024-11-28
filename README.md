
[![Deploy Azure Resources](https://github.com/sangamdeuja/mlops/actions/workflows/iac-pipeline-tf.yml/badge.svg)](https://github.com/sangamdeuja/mlops/actions/workflows/iac-pipeline-tf.yml)
[![Deploy Model Training Pipeline](https://github.com/sangamdeuja/mlops/actions/workflows/deploy-model-training-pipeline-classical.yml/badge.svg)](https://github.com/sangamdeuja/mlops/actions/workflows/deploy-model-training-pipeline-classical.yml)
[![Deploy and Test Online Endpoint and Deployment](https://github.com/sangamdeuja/mlops/actions/workflows/deploy-online-endpoint-pipeline-classical.yml/badge.svg)](https://github.com/sangamdeuja/mlops/actions/workflows/deploy-online-endpoint-pipeline-classical.yml)

#  Getting started with Azure MLOps (based on enterprise grade solution from [Azure MLOps (v2) Solution Accelerator](https://github.com/Azure/mlops-v2) )
## Challenges during implementing V2 using terraform, github action and Azure cli version 2
- Azure Free Account or Azure for Students versions do not work as they lack access at the subscription level for authorization, and you are not eligible to request VM quotas. Therefore, you need to have your own subscription and ensure you are eligible to request VM quotas in the region where you are working.
- V2 combines multiple repositories to run workflows, making it challenging to navigate the codebase.
- V2 is an excellent reference for those with some experience who understand the concepts and can modify the setup as needed. Microsoft provides comprehensive [documentation](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-github-azure-ml?view=azureml-api-2&tabs=azure-shell) for its implementation.
- And yet, there are still several challenges you may encounter during implementation. For instance, the training pipeline and online deployment pipeline may fail due to issues with building the container image on top of the provided base image, often caused by dependency conflicts.

This repository guides you through orchestrating an Azure ML workspace, performing classical ML training, and deploying an online endpoint using a similar template and the same data as in V
## Using this repo
### Pre-requisites 
- basic knowledge in azure cloud, azure ML and azure cli
- [What terrarom is](https://developer.hashicorp.com/terraform/intro)
- basic understanding of [github action](https://docs.github.com/en/actions/writing-workflows/quickstart)
- [docker basics](https://docs.docker.com/get-started/) to understand how containers are used inside azure ml and for debugging
- needs to have pay-as-you-go subscription, and git installed, enoguh quotas of azureml instance to deploy endpoint
- tools: azure cli, docker and terraform installed(for debugging). These installations are optional but they might be very useful for debugging

### Limitations
- Does not implement [AzureML-Observability](https://techcommunity.microsoft.com/blog/machinelearningblog/azureml-observability-a-scalable-and-extensible-solution-for-ml-monitoring-and-d/3474066)
- There is a single main branch, and no separate production or development environments have been created. GitHub workflows need to be triggered manually.
- No dynamic variable names are used. So, rerunning the pipelines throws an error. eg. during resource creation, online-endpoint creation etc.
    - if you want to rerun all workflows, delete the resource groups in azure portal. Also, make sure to permanently delete the deleted resources especially ml workspace and key-vault.
    - if you just want to run the online-deployment, delete the existing endpoint and modify the endpoint name in source code. 


### Instructions
- clone this repo
- modify the variables in infrastructure/terraform.tfvars 
- push the code in your github
- create service principle using App registration and assign contributor role at subscription level.
- Create client secret and save the value
- Store the repository secrets in github. Impelementing steps 4-6 is also described in [this link](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-github-azure-ml?view=azureml-api-2&tabs=azure-portal)
- You are now ready to experiment. Go to Actions in Github and it will have 3 workflows.
    - select the Deploy Azure Resources workflow and click run workflow. It takes sometime to provision you your ml workspace. Once the resource are deployed verify them from azure portal/cli
    - select the Deploy Model Training Pipeline and click run workflow. It takes a bit long time to provision your docker environment and initiate the training pipeline. Once the workflow completes, go to your azure ml workspace in the portal and select pipeline and navigate different components in UI, if you want to check the logs double click the component and check the logs. Those components turns green from gray-->blue-->geen which indicates the run is successful. If you see red then there are some issue. You can check the logs. Make sure the pipeline run is successful.
    - Finally, select the Deploy and Test Online Endpoint and Deployment and click run workflow. If the run is successful you will have a working endpoint. You can test the online endpoint from the portal as described in the same link as in step 6 

## Debugging
### Debugging Deploy Azure Resources Workflow
- In this part, if there is any issue, read the error message in github workflow carefully. Generally, error may occur due to naming convention described in azure documentation such as global unique names, characters limitations etc. Modify the variables in infrastructure/terraform.tfvars
- you can test it locally. Make sure you have terraform installed and cofnfigured. Try running terraform init, terraform plan within mlops/infrastructure folder. Make sure to delete the changes caused by terraform or simply use .gitignore

### Debugging Deploy Model Training Pipeline
- Issues may arise due to failure of creating docker image for training. Check the packages and versions in data-science/environment/train-conda.yml that fits the need. ALso you can check the logs from azure workspace-->pipelines-->outputs + logs
- You can test if the docker build works with your requirements locally. Create the docker image with your requirements on top of base image mentioned in mlops/azureml/train/train-env.yml. Make sure the build is successful(need to have some docker skills). If the image build fails you can check the logs. Make sure you create python virtual environment while implementing this step

### Debugging  Deploy and Test Online Endpoint and Deployment
- Again, the issue may arise due to already available enpoints,if so, delete the existing endpoint, modify the endpoint name in mlops/azureml/deploy/online-deployment.yml and in mlops/azureml/deploy/online-endpoint.yml. Push the code changes in github. Finally run the workflow.
- If the issue is from docker image build or score.py, the azureml provides testing and deploying the endpoint locally. For that, you need to download the trained model and check mlops/debug-online-deployment/test-local-deployment path for local testing or follow [this tutorial](https://www.youtube.com/watch?v=bue85m7lbjQ&ab_channel=KevinFeasel)

Final suggestion: If you are aware of all of these technologies and want to build your own from scartch, carefully check the file references in other files and how they are dependent and read more documentations.
- [Github actions workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [azureml cli](https://learn.microsoft.com/en-us/cli/azure/ml?view=azure-cli-latest)
- [azureml pipeline schema](https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-job-pipeline?view=azureml-api-2)
- [azureml environment setup](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-environments-v2?view=azureml-api-2&tabs=cli)
- [azureml online deployment schema](https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-deployment-managed-online?view=azureml-api-2)
- [azureml online endpoint schema](https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-endpoint-online?view=azureml-api-2)
- [azureml score script for online deployment](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2&tabs=cli)
- [debug score script](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-inference-server-http?view=azureml-api-2)
- [increase vm quotas](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-quotas?view=azureml-api-2)
