# swagger_client.RapidOrthophotosApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rapid_orthophoto_by_id**](RapidOrthophotosApi.md#get_rapid_orthophoto_by_id) | **GET** /v1/projects/{projectId}/rapidOrthophotos/{id} | 
[**get_rapid_orthophotos**](RapidOrthophotosApi.md#get_rapid_orthophotos) | **GET** /v1/projects/{projectId}/rapidOrthophotos | 

# **get_rapid_orthophoto_by_id**
> GlobalForesterApiV1ControllersRapidOrthophotosSharedResponseRapidOrthophoto get_rapid_orthophoto_by_id(project_id, id)



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
api_instance = swagger_client.RapidOrthophotosApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_rapid_orthophoto_by_id(project_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RapidOrthophotosApi->get_rapid_orthophoto_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GlobalForesterApiV1ControllersRapidOrthophotosSharedResponseRapidOrthophoto**](GlobalForesterApiV1ControllersRapidOrthophotosSharedResponseRapidOrthophoto.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rapid_orthophotos**
> list[GlobalForesterApiV1ControllersRapidOrthophotosSharedResponseRapidOrthophoto] get_rapid_orthophotos(project_id)



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
api_instance = swagger_client.RapidOrthophotosApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 

try:
    api_response = api_instance.get_rapid_orthophotos(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RapidOrthophotosApi->get_rapid_orthophotos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**list[GlobalForesterApiV1ControllersRapidOrthophotosSharedResponseRapidOrthophoto]**](GlobalForesterApiV1ControllersRapidOrthophotosSharedResponseRapidOrthophoto.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

