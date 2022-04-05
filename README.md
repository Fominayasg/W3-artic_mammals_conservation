# Artic fauna conservation

![picture](https://github.com/Fominayasg/W3-pipelines-project-artic_mammals/blob/main/Images/humpback-whale-436120.jpg)

This repository will analyze how the situation of various artic species has changed over the years.
It will focus primarily on marine mammals, specifically in whales.


## Primary dataset

The dataset was extracted from the website of the Ocean bioversity information system, better known as OBIS.

[Download link](https://mapper.obis.org/?datasetid=19119a0f-92f3-4662-85c5-30f8472067cf#)

The dataset showed data on the classification of the different species, the coordinates in which they had been seen and the date.
It had 23499 registers.

## Cleaning

The file collected information about the presence of multiple species over time.
After cleaning the dataset, the number of species was reduced only to marine mammals, creating a new file that can be found in the "data" folder.


## Enrichment

As the objective is to see if the species have changed their degree of threat, it was decided to enrich the data set using the IUCN API :IUCN 2020. IUCN Red List of Threatened Species. [Version 2020-3](https://apiv3.iucnredlist.org/api/v3/)

Historical data of the threat categories of each of the species were obtained from it and they were collected in a new data set also included in the "data" folder.

## Technology Stack
In this project we have used the following libraries:
 - [pandas](https://pandas.pydata.org/docs/)
 
 - [numpy](https://numpy.org/doc/stable/)
 
 - [seaborn](https://seaborn.pydata.org/)
 
 - our own [cleaning functions](https://github.com/Fominayasg/W3-pipelines-project-artic_mammals/blob/main/src/cleaning_magic.py)
 - our own [API functions](https://github.com/Fominayasg/W3-pipelines-project-artic_mammals/blob/main/src/api_functions.py) to enrich the data set with the IUCN API.