# Keys are variation names and the value is the ordinal
var_to_ord = {
    'Regular': '1'
}
api_token = 'Replace Me'

# Batch request. 30 max,
{
  "requests": [
    {
      "method": "POST",
      "relative_path": "/v1/LOCATION_ID/categories",
      "access_token": "ACCESS_TOKEN",
      "body": {
        "name": "Beverages"
      },
      "request_id": "MyRequestID"
    }
  ]
  }
# Batch response
[
  {
    "status_code": 200,
    "body": {
      "id": "36ac7016-3a4e-4934-81f1-9057ac613f2y",
      "name": "Beverages"
    },
    "request_id": "MyRequestID"
  }
  ]
