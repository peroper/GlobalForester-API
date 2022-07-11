# swagger_client.ProjectsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /v1/teams/{teamId}/projects/{projectId} | 
[**get_project**](ProjectsApi.md#get_project) | **GET** /v1/teams/{teamId}/projects/{projectId} | 
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /v1/teams/{teamId}/projects | 
[**post_project**](ProjectsApi.md#post_project) | **POST** /v1/teams/{teamId}/projects | 
[**put_project**](ProjectsApi.md#put_project) | **PUT** /v1/teams/{teamId}/projects/{projectId} | 

# **delete_project**
> delete_project(team_id, project_id)



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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
project_id = 'project_id_example' # str | 

try:
    api_instance.delete_project(team_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> GlobalForesterApiV1ControllersProjectsSharedResponseProject get_project(team_id, project_id)



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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
project_id = 'project_id_example' # str | 

try:
    api_response = api_instance.get_project(team_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

[**GlobalForesterApiV1ControllersProjectsSharedResponseProject**](GlobalForesterApiV1ControllersProjectsSharedResponseProject.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[GlobalForesterApiV1ControllersProjectsSharedResponseProject] get_projects(team_id)



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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    api_response = api_instance.get_projects(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**list[GlobalForesterApiV1ControllersProjectsSharedResponseProject]**](GlobalForesterApiV1ControllersProjectsSharedResponseProject.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project**
> GlobalForesterApiV1ControllersProjectsSharedResponseProject post_project(team_id, body=body)



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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersProjectsPostProjectRequestProject() # GlobalForesterApiV1ControllersProjectsPostProjectRequestProject |  (optional)

try:
    api_response = api_instance.post_project(team_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->post_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersProjectsPostProjectRequestProject**](GlobalForesterApiV1ControllersProjectsPostProjectRequestProject.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersProjectsSharedResponseProject**](GlobalForesterApiV1ControllersProjectsSharedResponseProject.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project**
> GlobalForesterApiV1ControllersProjectsSharedResponseProject put_project(team_id, project_id, body=body)



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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
project_id = 'project_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersProjectsPutProjectRequestProject() # GlobalForesterApiV1ControllersProjectsPutProjectRequestProject |  (optional)

try:
    api_response = api_instance.put_project(team_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->put_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **project_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersProjectsPutProjectRequestProject**](GlobalForesterApiV1ControllersProjectsPutProjectRequestProject.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersProjectsSharedResponseProject**](GlobalForesterApiV1ControllersProjectsSharedResponseProject.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

