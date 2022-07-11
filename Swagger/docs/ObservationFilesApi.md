# swagger_client.ObservationFilesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image**](ObservationFilesApi.md#get_image) | **GET** /v1/observations/{observationId}/images/{id} | 
[**get_observation_files**](ObservationFilesApi.md#get_observation_files) | **GET** /v1/observations/{observationId}/files | 

# **get_image**
> get_image(observation_id, id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Authorization Code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Client Credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ObservationFilesApi(swagger_client.ApiClient(configuration))
observation_id = 'observation_id_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.get_image(observation_id, id)
except ApiException as e:
    print("Exception when calling ObservationFilesApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observation_files**
> list[GlobalForesterApiV1ControllersObservationFilesSharedResponseObservationFile] get_observation_files(observation_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Authorization Code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Client Credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ObservationFilesApi(swagger_client.ApiClient(configuration))
observation_id = 'observation_id_example' # str | 

try:
    api_response = api_instance.get_observation_files(observation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservationFilesApi->get_observation_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_id** | **str**|  | 

### Return type

[**list[GlobalForesterApiV1ControllersObservationFilesSharedResponseObservationFile]**](GlobalForesterApiV1ControllersObservationFilesSharedResponseObservationFile.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

