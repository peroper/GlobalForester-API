# swagger_client.ObservationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_observation**](ObservationsApi.md#delete_observation) | **DELETE** /v1/projects/{projectId}/observations/{observationId} | 
[**get_observation**](ObservationsApi.md#get_observation) | **GET** /v1/projects/{projectId}/observations/{observationId} | 
[**get_observations**](ObservationsApi.md#get_observations) | **GET** /v1/projects/{projectId}/observations | 
[**post_observation**](ObservationsApi.md#post_observation) | **POST** /v1/projects/{projectId}/observations | 
[**put_observation**](ObservationsApi.md#put_observation) | **PUT** /v1/projects/{projectId}/observations/{observationId} | 

# **delete_observation**
> delete_observation(project_id, observation_id)



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
api_instance = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
observation_id = 'observation_id_example' # str | 

try:
    api_instance.delete_observation(project_id, observation_id)
except ApiException as e:
    print("Exception when calling ObservationsApi->delete_observation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **observation_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observation**
> GlobalForesterApiV1ControllersObservationsSharedResponseObservation get_observation(project_id, observation_id)



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
api_instance = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
observation_id = 'observation_id_example' # str | 

try:
    api_response = api_instance.get_observation(project_id, observation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservationsApi->get_observation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **observation_id** | **str**|  | 

### Return type

[**GlobalForesterApiV1ControllersObservationsSharedResponseObservation**](GlobalForesterApiV1ControllersObservationsSharedResponseObservation.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observations**
> list[GlobalForesterApiV1ControllersObservationsSharedResponseObservation] get_observations(project_id)



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
api_instance = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 

try:
    api_response = api_instance.get_observations(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservationsApi->get_observations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**list[GlobalForesterApiV1ControllersObservationsSharedResponseObservation]**](GlobalForesterApiV1ControllersObservationsSharedResponseObservation.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_observation**
> GlobalForesterApiV1ControllersObservationsSharedResponseObservation post_observation(project_id, body=body)



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
api_instance = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersObservationsPostObservationRequestObservation() # GlobalForesterApiV1ControllersObservationsPostObservationRequestObservation |  (optional)

try:
    api_response = api_instance.post_observation(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservationsApi->post_observation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersObservationsPostObservationRequestObservation**](GlobalForesterApiV1ControllersObservationsPostObservationRequestObservation.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersObservationsSharedResponseObservation**](GlobalForesterApiV1ControllersObservationsSharedResponseObservation.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_observation**
> GlobalForesterApiV1ControllersObservationsSharedResponseObservation put_observation(project_id, observation_id, body=body)



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
api_instance = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
observation_id = 'observation_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersObservationsPutObservationRequestObservation() # GlobalForesterApiV1ControllersObservationsPutObservationRequestObservation |  (optional)

try:
    api_response = api_instance.put_observation(project_id, observation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservationsApi->put_observation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **observation_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersObservationsPutObservationRequestObservation**](GlobalForesterApiV1ControllersObservationsPutObservationRequestObservation.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersObservationsSharedResponseObservation**](GlobalForesterApiV1ControllersObservationsSharedResponseObservation.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

