[![Install](https://github.com/jc39963/jdc154_polars/actions/workflows/hello.yml/badge.svg)](https://github.com/jc39963/jdc154_polars/actions/workflows/hello.yml)

[![Lint](https://github.com/jc39963/jdc154_polars/actions/workflows/lint.yml/badge.svg)](https://github.com/jc39963/jdc154_polars/actions/workflows/lint.yml)

[![Format](https://github.com/jc39963/jdc154_polars/actions/workflows/format.yml/badge.svg)](https://github.com/jc39963/jdc154_polars/actions/workflows/format.yml)

[![Test](https://github.com/jc39963/jdc154_polars/actions/workflows/test.yml/badge.svg)](https://github.com/jc39963/jdc154_polars/actions/workflows/test.yml)

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

![image](https://github.com/user-attachments/assets/42e7c45c-df9c-4092-a18d-d262369121aa)

## Check format and test errors
1. Format code `make format`
![image](https://github.com/user-attachments/assets/d4af6bf3-585f-4cdd-b6e4-911dfc0f3529)

2. Lint code `make lint`
![image](https://github.com/user-attachments/assets/64b3ef60-438f-41b2-8ad3-0c1cf339ac58)

3. Test code `make test`
![image](https://github.com/user-attachments/assets/7a88efb3-e309-4499-83c1-d98adbfd4295)

(alternatively, do all with `make all`)




