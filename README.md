# MSDS436 - Final Project
This repository contains code used for MSDS 436 Final Project

## Table of Contents
- [Introduction](#introduction)
- [About the Data](#about-the-data)
  * [Divvy Ride Data](#divvy-ride-data)
  * [Open Source Routing Machine (OSRM) API](#open-source-routing-machine-(osrm)-api)
  * [OpenWeather API](#openweather-api)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Project Details](#project-details)
- [EDA](#eda)
- [Models](#models)
- [Future Enhancements](#future-enhancements)
- [Troubleshooting & FAQ](#troubleshooting-&-faq)
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
- Requiremnt.txt

## Configuration

## Project Details

## EDA

## Models
The first ML objective of the project was to use divvy ride and weather data to identify opportunities for internal cost savings, and to predict station over and under supply to anticipate bike transfer needs.

To identify internal cost saving opportunities, we aggregate daily departures and arrivals by station for the month of September. We then collect the maximum daily departure and maximum daily arrival for each station, and identify stations with a maximum departure and arrival of less than or equal to two for the entire month of September. We identify these stations as “low-traffic stations,” and export this list of 480 stations for consideration for closure. To make a final decision, however, we recommend an analysis of year-round data to account for seasonal trends that may influence station usage.

To anticipate bike transfer needs, we identify mid- to high-traffic stations using the same methodology as explained above. We focus the remainder of our analysis on these higher traffic stations, assuming their traffic will contribute to station supply and shortage most meaningfully. In total, 481 stations were selected.

After correlation and autocorrelation analysis the following predictive features were selected for the model: weekday (binary), average daily temperature, average daily windspeed, total daily rain, day of the week, one-day ride count lag, two-day ride count lag, and a one-hot encoding of a weather description (“clear”, “clouds”, “drizzle”, “mist”, “rain”, “thunderstorm” and “smoke”).

Two ordinary least squares regression was performed on each station: one for daily arrivals and one for daily departures. These predictions were pushed into a single data frame and their differentials calculated. The forecasted differential identifies stations with a predicted overage supply, and stations with a predicted bike shortage—these forecasts will inform bike relocation efforts, and prevent lost rental opportunities due to bike shortage at high-demand stations.

We recommend the next step of this project be to use the latitude and longitude station data to identify station proximity, and recommend bike movement between stations with overage and shortage within close physical proximity—furthering cost saving efforts.

## Future Enhancements

## Troubleshooting & FAQ


## Project Owners
- [Katie Gaertner](https://github.com/katiegaertner)
- [Carlin Gerstenberger](https://github.com/carlin-gerstenberger)
- [Nicholas Drake](https://github.com/DrakeData)
