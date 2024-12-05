# Table of Contents
- Installation
    - [Cloud Technology](#cloud-technology)
    - [Raspberry Pi (Optional)](#raspberry-pi-optional)
- Running the Program
    - [Local Machine](#local-machine)
    - [Google Cloud Console](#google-cloud-console)
    - [Raspberry Pi (Optional)](#raspberry-pi-optional-1)
- [Result](#result)
---

# Installation 
## Cloud Technology
- Download [Terraform](https://developer.hashicorp.com/terraform/install)
- Create a Google Cloud Platform account
- Create a project named **terraform** and id of  **terraform-441517**
- Go to *Compute Engine* in the search bar and click *Enable*, if it's not already enabled
- Go to *Service accounts* in the search bar
and click *CREATE SERVICE ACCOUNT* which is below the search search bar
- Name the service account, anything
-  Give the service account the role of *Compute Admin* and *Bigtable Administrator*
- Click *DONE*
- Under *Actions* which is to the rightmost of your screen, click the three dots, then click *Manage keys*
- Click *ADD KEY*, then *Create new key*
- Select *JSON*
- A JSON file will be download which holds your key to access Google Cloud Platform 
- Name the JSON file **terraform-441517-7c57012e3f82.json**
- Move **terraform-441517-7c57012e3f82.json** into the **IaC** folder of the repo

## Raspberry Pi (Optional)
Configuring the Raspberry Pi is optional. Everything else will run fine without the Raspberry Pi. If configuring the Raspberry, I'll assume you already SSH into the Raspberry Pi and the Sense HAT is installed.

- Make sure the Raspberry Pi is up-to-date
    - ```sudo apt-get update && sudo apt-get upgrade```
- Install the Python packages
    - ```sudo apt-get install sense-hat python3-numpy python3-websocket```
    - ```sudo pip3 install google-cloud-bigtable --break-system-packages```

Restart the Raspberry Pi, just in case
- ```sudo reboot```

---

# Running the Program
## Local Machine
- Clone this repo onto your local machine
    - ```https://github.com/Kdot729/Heatmap-Raspberry-Pi.git```
- In the root directory of the repo, change directory
    - ```cd IaC```
- [Make sure **terraform-441517-7c57012e3f82.json** is in the **IaC**](#L33)
- Initialize Terraform
    - ```terraform init```
- Apply Terraform
    - ```terraform apply –auto-approve```

## Google Cloud Console
- After running the steps on your [local machine](#local-machine)
- Go to the Google Cloud Console
- Click on the instance, *ubuntu-docker*, then click *SSH*
- Inside the GCP shell, upload the file **terraform-441517-7c57012e3f82.json** that's on your local machine
- Copy terraform-441517-7c57012e3f82.json into the necessary folders in Compute Engine
    - ```sudo cp terraform-441517-7c57012e3f82.json /Heatmap-Raspberry-Pi/raspberry && sudo cp terraform-441517-7c57012e3f82.json /Heatmap-Raspberry-Pi/api && sudo cp terraform-441517-7c57012e3f82.json /Heatmap-Raspberry-Pi/cloud_database```
- Edit the IP address in a file
    - ```sudo nano /Heatmap-Raspberry-Pi/frontend/src/scripts/fetch.js```
    - Find the string *http://127.0.0.1:8000* and replace *127.0.0.1* with the external IP, which can be seen in the *VM instances*
- Verify Docker is installed in GCP shell
    - ```docker –version```
- After confirming docker is installed, build the containers
    - ```cd /Heatmap-Raspberry-Pi && sudo docker compose up --build -d```

## Raspberry Pi (Optional)
- If you configured the Raspberry Pi in the section, [Raspberry Pi](#raspberry-pi-optional)
- Clone this repo onto the Raspberry Pi
    - ```https://github.com/Kdot729/Heatmap-Raspberry-Pi.git```
- In the root directory of the repo, change directory
    - ```cd raspberry```
- On your local machine, copy the contents of **terraform-441517-7c57012e3f82.json**
- Create terraform-441517-7c57012e3f82.json
    - ```nano terraform-441517-7c57012e3f82.json```
    - Paste the contents
    - Save the file
- Set an environment variable
    - ```export GOOGLE_APPLICATION_CREDENTIALS="terraform-441517-7c57012e3f82.json```
- Run the code related to the Raspberry Pi with ```python3 main.py```

# Result
- Once the containers are running and you ran the main.py in the Raspberry Pi
- You'll see the Sense HAT changing color, each pixel representing the amount of Ethereum traded per second
- You can go the the external IP with port 3000, to see a table showing the amount of Ethereum traded per second
- The url will be in the format of url *http://"external IP":3000*, replacing "external IP" with the external IP of Compute Engine
- Once you're done, in the *Iac* folder, destroy everything
    - ```terraform destroy --auto-approve```