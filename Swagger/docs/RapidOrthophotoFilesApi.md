# swagger_client.RapidOrthophotoFilesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rapid_orthophoto_files**](RapidOrthophotoFilesApi.md#get_rapid_orthophoto_files) | **GET** /v1/rapidOrthophotos/{rapidOrthophotoId}/files | 
[**get_rapid_orthophoto_geo_package**](RapidOrthophotoFilesApi.md#get_rapid_orthophoto_geo_package) | **GET** /v1/rapidOrthophotos/{rapidOrthophotoId}/geoPackages/{id} | 
[**get_rapid_orthophoto_originals**](RapidOrthophotoFilesApi.md#get_rapid_orthophoto_originals) | **GET** /v1/rapidOrthophotos/{rapidOrthophotoId}/originals/{id} | 

# **get_rapid_orthophoto_files**
> list[GlobalForesterApiV1ControllersRapidOrthophotoFilesSharedResponseRapidOrthophotoFile] get_rapid_orthophoto_files(rapid_orthophoto_id)



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
api_instance = swagger_client.RapidOrthophotoFilesApi(swagger_client.ApiClient(configuration))
rapid_orthophoto_id = 'rapid_orthophoto_id_example' # str | 

try:
    api_response = api_instance.get_rapid_orthophoto_files(rapid_orthophoto_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RapidOrthophotoFilesApi->get_rapid_orthophoto_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rapid_orthophoto_id** | **str**|  | 

### Return type

[**list[GlobalForesterApiV1ControllersRapidOrthophotoFilesSharedResponseRapidOrthophotoFile]**](GlobalForesterApiV1ControllersRapidOrthophotoFilesSharedResponseRapidOrthophotoFile.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rapid_orthophoto_geo_package**
> get_rapid_orthophoto_geo_package(rapid_orthophoto_id, id)



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
api_instance = swagger_client.RapidOrthophotoFilesApi(swagger_client.ApiClient(configuration))
rapid_orthophoto_id = 'rapid_orthophoto_id_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.get_rapid_orthophoto_geo_package(rapid_orthophoto_id, id)
except ApiException as e:
    print("Exception when calling RapidOrthophotoFilesApi->get_rapid_orthophoto_geo_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rapid_orthophoto_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geopackage+sqlite3

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rapid_orthophoto_originals**
> get_rapid_orthophoto_originals(rapid_orthophoto_id, id)



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
api_instance = swagger_client.RapidOrthophotoFilesApi(swagger_client.ApiClient(configuration))
rapid_orthophoto_id = 'rapid_orthophoto_id_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.get_rapid_orthophoto_originals(rapid_orthophoto_id, id)
except ApiException as e:
    print("Exception when calling RapidOrthophotoFilesApi->get_rapid_orthophoto_originals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rapid_orthophoto_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

