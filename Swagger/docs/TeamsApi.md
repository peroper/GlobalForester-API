# swagger_client.TeamsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_team**](TeamsApi.md#delete_team) | **DELETE** /v1/teams/{teamId} | 
[**get_team**](TeamsApi.md#get_team) | **GET** /v1/teams/{teamId} | 
[**get_teams**](TeamsApi.md#get_teams) | **GET** /v1/teams | 
[**post_team**](TeamsApi.md#post_team) | **POST** /v1/teams | 
[**put_team**](TeamsApi.md#put_team) | **PUT** /v1/teams/{teamId} | 

# **delete_team**
> delete_team(team_id)



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
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    api_instance.delete_team(team_id)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> GlobalForesterApiV1ControllersTeamsSharedResponseTeam get_team(team_id)



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
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    api_response = api_instance.get_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**GlobalForesterApiV1ControllersTeamsSharedResponseTeam**](GlobalForesterApiV1ControllersTeamsSharedResponseTeam.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> list[GlobalForesterApiV1ControllersTeamsSharedResponseTeam] get_teams()



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
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GlobalForesterApiV1ControllersTeamsSharedResponseTeam]**](GlobalForesterApiV1ControllersTeamsSharedResponseTeam.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_team**
> GlobalForesterApiV1ControllersTeamsSharedResponseTeam post_team(body=body)



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
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GlobalForesterApiV1ControllersTeamsPostTeamRequestTeam() # GlobalForesterApiV1ControllersTeamsPostTeamRequestTeam |  (optional)

try:
    api_response = api_instance.post_team(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->post_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlobalForesterApiV1ControllersTeamsPostTeamRequestTeam**](GlobalForesterApiV1ControllersTeamsPostTeamRequestTeam.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersTeamsSharedResponseTeam**](GlobalForesterApiV1ControllersTeamsSharedResponseTeam.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_team**
> GlobalForesterApiV1ControllersTeamsSharedResponseTeam put_team(team_id, body=body)



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
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 
body = swagger_client.GlobalForesterApiV1ControllersTeamsPutTeamRequestTeam() # GlobalForesterApiV1ControllersTeamsPutTeamRequestTeam |  (optional)

try:
    api_response = api_instance.put_team(team_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->put_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **body** | [**GlobalForesterApiV1ControllersTeamsPutTeamRequestTeam**](GlobalForesterApiV1ControllersTeamsPutTeamRequestTeam.md)|  | [optional] 

### Return type

[**GlobalForesterApiV1ControllersTeamsSharedResponseTeam**](GlobalForesterApiV1ControllersTeamsSharedResponseTeam.md)

### Authorization

[Authorization Code](../README.md#Authorization Code), [Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

