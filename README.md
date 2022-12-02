# MSDS436 - Final Project
This repository contains code used for MSDS 436 Final Project

## Table of Contents
- [Introduction](#introduction)
- [About the Data](#about-the-data)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Project Details](#project-details)
- [Architecture](#architecture)
- [EDA](#eda)
- [Models](#models)
- [Future Enhancements](#future-enhancements)
- [Project Owners](#project-owners)

## Introduction
As a leading bike share service in the city of Chicago, [Divvy's data](https://ride.divvybikes.com/system-data) offers unique opportunities to model human flow patterns.
Our internal team will leverage Divvy's data to create insights into human movement in Chicago.

These insights will directly increase Divvy's enterprise value through internal projects and resale opportunities.

## About the Data
### Divvy Ride Data

![divvy_logo](images/divvy_logo.jpg)

The Divvy bike data set is provided by Divvy on a monthly bases and can be found on [their website](https://ride.divvybikes.com/system-data).

The data contains trip information such as:
- Trip start day and time
- Trip end day and time
- Trip start station
- Trip end station
- Rider type (Member, Single Ride, and Day Pass)

For our usecase, we have limited the data set to only the month of September 2022 and rides that only have a start and end station. 
We have also taken a random sample of 5,000 rides per day.

### Open Source Routing Machine (OSRM) API

![osrm_logo](images/osrm_logo.png)

To get estimated trip time, we used the [OSRM API](http://project-osrm.org/docs/v5.10.0/api/#general-options). This API combines sophisticated routing algorithms with the open and free road network data of the OpenStreetMap (OSM) project. To calulate the shortest path for a bike ride, we pass the start and end station's latitude and longitude to return the estimated duration (in seconds) and distance (in meters).

### OpenWeather API

![openweather_logo](images/openweather_logo.jpg)

To gather historical weather data, we used [OpenWeather's One Call API](https://openweathermap.org/api/one-call-3#data). 
            
We gathered the following data points from the API:
- Tempature (in Fahrenheit)
- Humidity
- Wind Speed
- Weather
- Precipitation of rain/snow

Due to the cost per call model, we decided to limit our cost by only using the latitude and longitude of the center of Chicago (41.87, -87.62) and only pulling back 24 hours of data per day (total of 720 API calls).

## Requirements
(Need to update)
- API Key from OpenWeather
- AWS Account
- [PostgreSQL (Desktop)](https://www.postgresql.org/)
- Requiremnt.txt

## Configuration

## Project Details
For this project, we will be building an end-to-end process of gathering, preparing data for Machine Learning (ML) modeling using AWS platform, Python, and Spark.

## Architecture
Here is an overview for our project architecture:

![project_arch](images/project_arch.png)

### Step 1: Gather the data
We first needed to extract the necisary data from Divvy's website, make API calls to OSRM and OpenWeather API, and clean the data set

### Step 2: Load csv file into AWS S3 Bucket
To create an Amazon Simple Storage Service (S3) bucket, we needed to set up an [AWS account](https://aws.amazon.com/) and then [setup the S3 bucket](https://www.sqlshack.com/getting-started-with-amazon-s3-and-python/). The bucket name for our S3 bucket is `msds436-final`. 

Using Python, we were able to automate this proces to load the created csv files into our S3 bucket. The Python script creates a folder called `files` in the S3 bucket and saves the csv file in it.

**Python example:**

![python_s3_example](images/python_s3_load.PNG)

**File in S3:**

![s3_file](images/aws_s3.PNG)

### Step 3: Spin up PostgreSQL server to use as our Data Lake (DL), create a relational data model and load the curated data from S3 buckets.

- To spin up a PostgreSQL server, follow this helpful AWS resources: 
    * Document: [Create and Connect to a PostgreSQL Database
with Amazon RDS](https://aws.amazon.com/getting-started/hands-on/create-connect-postgresql-db/)
    * YouTube Video: [AWS RDS Aurora Postgres Database Setup | Step by Step Tutorial](https://youtu.be/vw5EO5Jz8-8)

**NOTE:** Make sure to add these inbound security rules:
    
![aws_sr](images/aws_sr.PNG)

- Once your PostgreSQL server is available, open up pgAdmin and add a new server.

![aws_active_db](images/aws_active_db.PNG)
![paAdmin_Connect](images/pgadmin_connect.PNG)

- Using pgAdmin Query Tool, install `aws_commmon' by run:
    
        CREATE EXTENSION aws_s3 CASCADE;

![pgAdmin](images/pgadmin_qtool.PNG)

- Then create table called `bike_data`:
       
        CREATE TABLE bike_data (ride_id varchar(120) primary key,
					rideable_type varchar(120) NOT NULL,
					started_at date,
					ended_at date,
					start_station_name varchar(120) NOT NULL,
					start_station_id varchar(120) NOT NULL,
					end_station_name varchar(120) NOT NULL,
					end_station_id varchar(120) NOT NULL, 
					start_lat numeric,
					start_lng numeric,
					end_lat numeric,
					end_lng numeric,
					member_casual varchar(120),
					started_at_clean date,
					duration numeric,
					distance numeric,
					started_at_unix integer,
					temp numeric,
					hum numeric,
					windsp numeric,
					weather varchar(120),
					rain numeric,
					snow numeric
					);
    
- Using pgAdmin, load data from S3 to Postgres

        SELECT aws_s3.table_import_from_s3('bike_data', 'ride_id,rideable_type,started_at,ended_at,start_station_name,start_station_id,end_station_name,end_station_id,start_lat,start_lng,end_lat,end_lng,member_casual,started_at_clean,duration,distance,started_at_unix,temp,hum,windsp,weather,rain,snow',
        '(format csv, header true)',
        'msds436-final',
        'files/202209_divvy_distance_weather.csv',
        'us-east-2',
        'YOUR_AWS_ACCESS_KEY', 
        'YOUR_AWS_SECRET_KEY' 
        );

- You will now be able to query the DL using Python.

**EXAMPLE:**

![python_query](images/python_q_dl.PNG)

## EDA

## Models
The first ML objective of the project was to use divvy ride and weather data to identify opportunities for internal cost savings, and to predict station over and under supply to anticipate bike transfer needs.

To identify internal cost saving opportunities, we aggregate daily departures and arrivals by station for the month of September. We then collect the maximum daily departure and maximum daily arrival for each station, and identify stations with a maximum departure and arrival of less than or equal to two for the entire month of September. We identify these stations as “low-traffic stations,” and export this list of 480 stations for consideration for closure. To make a final decision, however, we recommend an analysis of year-round data to account for seasonal trends that may influence station usage.

To anticipate bike transfer needs, we identify mid- to high-traffic stations using the same methodology as explained above. We focus the remainder of our analysis on these higher traffic stations, assuming their traffic will contribute to station supply and shortage most meaningfully. In total, 481 stations were selected.

After correlation and autocorrelation analysis the following predictive features were selected for the model: weekday (binary), average daily temperature, average daily windspeed, total daily rain, day of the week, one-day ride count lag, two-day ride count lag, and a one-hot encoding of a weather description (“clear”, “clouds”, “drizzle”, “mist”, “rain”, “thunderstorm” and “smoke”).

Two ordinary least squares regression was performed on each station: one for daily arrivals and one for daily departures. These predictions were pushed into a single data frame and their differentials calculated. The forecasted differential identifies stations with a predicted overage supply, and stations with a predicted bike shortage—these forecasts will inform bike relocation efforts, and prevent lost rental opportunities due to bike shortage at high-demand stations.

We recommend the next step of this project be to use the latitude and longitude station data to identify station proximity, and recommend bike movement between stations with overage and shortage within close physical proximity—furthering cost saving efforts.

## Future Enhancements

## Project Owners
- [Katie Gaertner](https://github.com/katiegaertner)
- [Carlin Gerstenberger](https://github.com/carlin-gerstenberger)
- [Nicholas Drake](https://github.com/DrakeData)
