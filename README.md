[![Install](https://github.com/nogibjj/jdc154_Descriptive_Stats/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/jdc154_Descriptive_Stats/actions/workflows/hello.yml)

[![Lint](https://github.com/nogibjj/jdc154_Descriptive_Stats/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/jdc154_Descriptive_Stats/actions/workflows/lint.yml)

[![Format](https://github.com/nogibjj/jdc154_Descriptive_Stats/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/jdc154_Descriptive_Stats/actions/workflows/format.yml)

[![Test](https://github.com/nogibjj/jdc154_Descriptive_Stats/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/jdc154_Descriptive_Stats/actions/workflows/test.yml)

# Netflix Movie and TV Shows Project Overview

## About the Project
The purpose of this project is to generate descriptive statistics with Polars and look into trends of movie and TV show releases on Netflix over the years. 

### Summary Statistics of Movie and TV Show Release Years:

![alt text](image.png)


### Visualizations
![alt text](images/TV_ratings.png)

![alt text](images/Movie_ratings.png)

## Note on the repository and directions:
This project contains:
* requirements.txt detailing the requirements needed for this project
* Makefile to install requirements, lint, format, and test your code
* github actions with separate YAML files for Install, Lint, Format, and Test in the github workflows folder
* DockerFile and devcontainer for environment set up
* Jupyter notebook performing descriptive statistics with Polars
* main.py Python script for statistics and generating data visualizations using Polars
* test_main.py for Python testing scripts
* Summary pdf containing the walkthrough and conclusions found in the data analysis



## Preparation
1. Open codespaces 
2. Load repo to code spaces
2. Wait for installation of all requirements in requirements.txt

## Check format and test errors
1. Format code `make format`
![image](https://github.com/user-attachments/assets/7688b60a-9f2b-45a2-acf3-8a7f66f346e1)

2. Lint code `make lint`
![image](https://github.com/user-attachments/assets/a225ac16-a6f1-4460-bc94-c6f9f6eae799)

3. Test code `make test`
![image](https://github.com/user-attachments/assets/366e23c2-a513-400f-bb7d-900abbdd41b1)

(alternatively, do all with `make all`)




