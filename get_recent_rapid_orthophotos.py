"""Lists all Rapid Orthophotos updated after the point in time given as input.

Without input, orthophotos one week back in time are fetched.

The result is printed to standard output.
"""

import utils
from datetime import datetime, timedelta
import swagger_client
import argparse

#Parses command line arguments
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-u', '--updated_after', dest='updated_after', help='A point in time in UTC timezone, for example 2022-12-24T14:00:00Z')
args = parser.parse_args()

selected_updated_after = args.updated_after

if (selected_updated_after is None):
  updated_after = datetime.utcnow() - timedelta(weeks=1)
else:
  updated_after = datetime.fromisoformat(selected_updated_after.replace("Z", "+00:00"))

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
rapid_orthophotos_api = swagger_client.RapidOrthophotosApi(swagger_client.ApiClient(configuration))

result = ""
fetch_data = True

try:
    while(fetch_data):
      #Get list of rapid orthophotos after point in time
      orthophoto_response = rapid_orthophotos_api.get_rapid_orthophotos(updated_after=updated_after)

      for ortophoto in orthophoto_response.results:
          result += f'Name: {ortophoto.name},  Id: {ortophoto.id},  Created: {ortophoto.created},  Updated: {ortophoto.updated}\n'

      #If there is more orthophotos available, is_truncated in metadata is set to true
      fetch_data = orthophoto_response.metadata.is_truncated
      updated_after = orthophoto_response.metadata.continue_with_updated_after

except Exception as e:
    print("Exception when calling RapidOrthophotosApi->get_rapid_orthophotos: %s\n" % e)

print(result)
