# swagger_client.TracklogsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tracklog**](TracklogsApi.md#delete_tracklog) | **DELETE** /v1/projects/{projectId}/tracklogs/{tracklogId} | 
[**get_tracklog**](TracklogsApi.md#get_tracklog) | **GET** /v1/projects/{projectId}/tracklogs/{tracklogId} | 
[**get_tracklogs**](TracklogsApi.md#get_tracklogs) | **GET** /v1/projects/{projectId}/tracklogs | 
[**post_tracklog**](TracklogsApi.md#post_tracklog) | **POST** /v1/projects/{projectId}/tracklogs | 
[**put_tracklog**](TracklogsApi.md#put_tracklog) | **PUT** /v1/projects/{projectId}/tracklogs/{tracklogId} | 

# **delete_tracklog**
> delete_tracklog(project_id, tracklog_id)



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
api_instance = swagger_client.TracklogsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
tracklog_id = 'tracklog_id_example' # str | 

try:
    api_instance.delete_tracklog(project_id, tracklog_id)
except ApiException as e:
    print("Exception when calling TracklogsApi->delete_tracklog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tracklog_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracklog**
> GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog get_tracklog(project_id, tracklog_id)



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
api_instance = swagger_client.TracklogsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
tracklog_id = 'tracklog_id_example' # str | 

try:
    api_response = api_instance.get_tracklog(project_id, tracklog_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracklogsApi->get_tracklog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tracklog_id** | **str**|  | 

### Return type

[**GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog**](GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracklogs**
> list[GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog] get_tracklogs(project_id)



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
api_instance = swagger_client.TracklogsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 

try:
    api_response = api_instance.get_tracklogs(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracklogsApi->get_tracklogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**list[GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog]**](GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tracklog**
> GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog post_tracklog(project_id, body=body)



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
api_instance = swagger_client.TracklogsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersTracklogsPostTracklogRequestTracklog() # GlobalForesterApiV1ControllersTracklogsPostTracklogRequestTracklog |  (optional)

try:
    api_response = api_instance.post_tracklog(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracklogsApi->post_tracklog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersTracklogsPostTracklogRequestTracklog**](GlobalForesterApiV1ControllersTracklogsPostTracklogRequestTracklog.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog**](GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tracklog**
> GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog put_tracklog(project_id, tracklog_id, body=body)



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
api_instance = swagger_client.TracklogsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | 
tracklog_id = 'tracklog_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersTracklogsPutTracklogRequestTracklog() # GlobalForesterApiV1ControllersTracklogsPutTracklogRequestTracklog |  (optional)

try:
    api_response = api_instance.put_tracklog(project_id, tracklog_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracklogsApi->put_tracklog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tracklog_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersTracklogsPutTracklogRequestTracklog**](GlobalForesterApiV1ControllersTracklogsPutTracklogRequestTracklog.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog**](GlobalForesterApiV1ControllersTracklogsSharedResponseTracklog.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

