from OSApiClient.api_query import ApiQuery

session = {
    "loginName": "admin",
    "password": "xxx",
    "domainName": "openspecimen"
}

api = ApiQuery("https://my.openspecimen.net/openspecimen", session)

query = {
    "aql": "select cp.shortTitle from Participant p",
    "cpId": "123"
}

result = api.execute_query(query)
print(result)