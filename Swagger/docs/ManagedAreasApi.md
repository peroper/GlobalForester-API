# swagger_client.ManagedAreasApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_managed_area**](ManagedAreasApi.md#delete_managed_area) | **DELETE** /v1/teams/{teamId}/managedAreas/{managedAreaId} | 
[**get_managed_area**](ManagedAreasApi.md#get_managed_area) | **GET** /v1/teams/{teamId}/managedAreas/{managedAreaId} | 
[**get_managed_areas**](ManagedAreasApi.md#get_managed_areas) | **GET** /v1/teams/{teamId}/managedAreas | 
[**post_managed_area**](ManagedAreasApi.md#post_managed_area) | **POST** /v1/teams/{teamId}/managedAreas | 
[**put_managed_area**](ManagedAreasApi.md#put_managed_area) | **PUT** /v1/teams/{teamId}/managedAreas/{managedAreaId} | 

# **delete_managed_area**
> delete_managed_area(team_id, managed_area_id)



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
api_instance = swagger_client.ManagedAreasApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
managed_area_id = 'managed_area_id_example' # str | 

try:
    api_instance.delete_managed_area(team_id, managed_area_id)
except ApiException as e:
    print("Exception when calling ManagedAreasApi->delete_managed_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **managed_area_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_area**
> GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea get_managed_area(team_id, managed_area_id)



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
api_instance = swagger_client.ManagedAreasApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
managed_area_id = 'managed_area_id_example' # str | 

try:
    api_response = api_instance.get_managed_area(team_id, managed_area_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAreasApi->get_managed_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **managed_area_id** | **str**|  | 

### Return type

[**GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea**](GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_areas**
> list[GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea] get_managed_areas(team_id)



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
api_instance = swagger_client.ManagedAreasApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    api_response = api_instance.get_managed_areas(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAreasApi->get_managed_areas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**list[GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea]**](GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_managed_area**
> GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea post_managed_area(team_id, body=body)



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
api_instance = swagger_client.ManagedAreasApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea() # GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea |  (optional)

try:
    api_response = api_instance.post_managed_area(team_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAreasApi->post_managed_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea**](GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea**](GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_managed_area**
> GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea put_managed_area(team_id, managed_area_id, body=body)



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
api_instance = swagger_client.ManagedAreasApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
managed_area_id = 'managed_area_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersManagedAreasPutManagedAreaRequestManagedArea() # GlobalForesterApiV1ControllersManagedAreasPutManagedAreaRequestManagedArea |  (optional)

try:
    api_response = api_instance.put_managed_area(team_id, managed_area_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAreasApi->put_managed_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **managed_area_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersManagedAreasPutManagedAreaRequestManagedArea**](GlobalForesterApiV1ControllersManagedAreasPutManagedAreaRequestManagedArea.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea**](GlobalForesterApiV1ControllersManagedAreasSharedResponseManagedArea.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

