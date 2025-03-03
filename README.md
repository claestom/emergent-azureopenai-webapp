# Azure OpenAI & Web App Tutorial

**Purpose**  
This repository demonstrates how to integrate Azure OpenAI (GPT-4) into a Python application, focusing on seamless chatbot functionality and showcasing best practices for using OpenAI services on Azure.

**Goal**  
The main goal is to provide a clear example of how Azure OpenAI can be leveraged to build intelligent applications, emphasizing maintainability, scalability, and secure handling of credentials.

## How to get started?

Create following resources:

1. [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)
2. [Deploy a model](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal#deploy-a-model)
3. [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli)

### Local development

```
mkdir emergentproject2025; cd emergentproject2025
```
```
git clone https://github.com/claestom/emergent-azureopenai-webapp.git ; cd "emergent-azureopenai-webapp"
```
Create a new file to store secrets, called .env:
```
New-Item -Path . -Name ".env" -ItemType "File"
```
Open VS Code
```
code .
```
Open the .env file and add following content + the values:
```
AZURE_OPENAI_KEY = ""
AZURE_OPENAI_ENDPOINT = ""
```
Create and activate virtual environment:
```
python -m venv . ; .\Scripts\Activate.ps1
```
Install required libaries:
```
pip install -r requirements.txt
```
Run script locally:
```
python app.py
```
Test it out using a seperate terminal:
```
curl -X POST -H "Content-Type: application/json" -d "{\"query\": \"Explain me what Emergent Leuven is?\"}"  http://localhost:5000
```
Stop de application:
```
CTRL + C
```

### Build Docker image

**Open the Docker desktop**

Next run following command:
```
docker build -t azure-openai-flask-demo .
```
After image has been create, start it in a container:
```
docker run -it -d -p 5000:5000 azure-openai-flask-demo
```
### Push Docker image to Azure Container Registry in Azure

Login to your ACR
```
docker login <name>.azurecr.io
```
```
docker tag azure-openai-flask-demo <name>.azurecr.io/azure-openai-flask-demo
```
```
docker push <name>.azurecr.io/azure-openai-flask-demo
```

### Create WebApp and use the image stored in the ACR

More information [here](https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container?tabs=azure-cli&pivots=container-linux).

Test the WebbApp:
```
curl -X POST -H "Content-Type: application/json" -d "{\"query\": \"Explain me what Emergent Leuven is?\"}"  https://<WebbAppName>.azurewebsites.net/
```