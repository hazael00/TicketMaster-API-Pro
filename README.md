# picketer
Swagger spec based on Ticketmaster Discovery API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import picketer 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import picketer
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import picketer
from picketer.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyQueryParam
picketer.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# picketer.configuration.api_key_prefix['apikey'] = 'Bearer'
# create an instance of the API class
api_instance = picketer.AttractionsApi()
id = 'id_example' # str | Attraction ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try:
    # Get attraction details by ID
    api_response = api_instance.attraction_details(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttractionsApi->attraction_details: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://app.ticketmaster.com/discovery/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttractionsApi* | [**attraction_details**](docs/AttractionsApi.md#attraction_details) | **GET** /attractions/{id} | Get attraction details by ID
*AttractionsApi* | [**search_attractions**](docs/AttractionsApi.md#search_attractions) | **GET** /attractions | Search attractions
*ClassificationsApi* | [**classification_details**](docs/ClassificationsApi.md#classification_details) | **GET** /classifications/{id} | Get classification details by ID
*ClassificationsApi* | [**genre_details**](docs/ClassificationsApi.md#genre_details) | **GET** /classifications/genres/{id} | Get genre details by ID
*ClassificationsApi* | [**search_classifications**](docs/ClassificationsApi.md#search_classifications) | **GET** /classifications | Search classifications
*ClassificationsApi* | [**segment_details**](docs/ClassificationsApi.md#segment_details) | **GET** /classifications/segments/{id} | Get segment details by ID
*ClassificationsApi* | [**subgenre_details**](docs/ClassificationsApi.md#subgenre_details) | **GET** /classifications/subgenres/{id} | Get subgenre details by ID
*EventsApi* | [**event_details**](docs/EventsApi.md#event_details) | **GET** /events/{id} | Get event details by ID
*EventsApi* | [**event_images**](docs/EventsApi.md#event_images) | **GET** /events/{id}/images | Get event images
*EventsApi* | [**search_events**](docs/EventsApi.md#search_events) | **GET** /events | Event search
*VenuesApi* | [**search_venues**](docs/VenuesApi.md#search_venues) | **GET** /venues | Venue search
*VenuesApi* | [**venue_details**](docs/VenuesApi.md#venue_details) | **GET** /venues/{id} | Get venue details by ID


## Documentation For Models

 - [Access](docs/Access.md)
 - [Address](docs/Address.md)
 - [Area](docs/Area.md)
 - [Attraction](docs/Attraction.md)
 - [BoxOfficeInfo](docs/BoxOfficeInfo.md)
 - [Chronology](docs/Chronology.md)
 - [City](docs/City.md)
 - [Classification](docs/Classification.md)
 - [ClassificationType](docs/ClassificationType.md)
 - [Container](docs/Container.md)
 - [Country](docs/Country.md)
 - [DMA](docs/DMA.md)
 - [Dates](docs/Dates.md)
 - [Duration](docs/Duration.md)
 - [Embedded](docs/Embedded.md)
 - [EndTime](docs/EndTime.md)
 - [Event](docs/Event.md)
 - [EventImages](docs/EventImages.md)
 - [Field](docs/Field.md)
 - [FieldType](docs/FieldType.md)
 - [GeneralInfo](docs/GeneralInfo.md)
 - [Genre](docs/Genre.md)
 - [GenreDetails](docs/GenreDetails.md)
 - [Image](docs/Image.md)
 - [Link](docs/Link.md)
 - [Links](docs/Links.md)
 - [Location](docs/Location.md)
 - [Market](docs/Market.md)
 - [Page](docs/Page.md)
 - [Place](docs/Place.md)
 - [PresaleDate](docs/PresaleDate.md)
 - [Price](docs/Price.md)
 - [Promoter](docs/Promoter.md)
 - [PublicDate](docs/PublicDate.md)
 - [Sales](docs/Sales.md)
 - [SeatMap](docs/SeatMap.md)
 - [Segment](docs/Segment.md)
 - [SegmentDetails](docs/SegmentDetails.md)
 - [Social](docs/Social.md)
 - [State](docs/State.md)
 - [Status](docs/Status.md)
 - [SubGenre](docs/SubGenre.md)
 - [SubGenreDetails](docs/SubGenreDetails.md)
 - [Time](docs/Time.md)
 - [TimeValue](docs/TimeValue.md)
 - [Twitter](docs/Twitter.md)
 - [Type](docs/Type.md)
 - [Venue](docs/Venue.md)
 - [Zone](docs/Zone.md)


## Documentation For Authorization


## APIKeyQueryParam

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Author

git@edward.sh
