import os

from dotenv import load_dotenv

from osapiclient import ApiQuery

# Load the variables from .env into the environment
load_dotenv()

# get env vars
loginname = os.getenv("APIUSER")
pwd = os.getenv("APIPW")
osurl = os.getenv("APIURL")

session = {
    "loginName": loginname,
    "password": pwd,
    "domainName": "openspecimen"
}

api = ApiQuery(osurl, session)

# query = {
#     "aql": "select cp.shortTitle from Participant p",
#     "cpId": "1"
# }
query = {
    "cpId": 1,
    "aql": "select Participant.id as \"$cprId\", Participant.ppid as \"Participant_ID\", Participant.regDate as \"Participant_Registration_Date\", Specimen.id as \"$specimenId\", CollectionProtocol.id as \"$cpId\", Specimen.label as \"Specimen_Label\", Specimen.type as \"Specimen_Type\", Specimen.tissueSite as \"Anatomic_Site\", Specimen.id as \"Identifier\", Specimen.lineage as \"Lineage\", Specimen.class as \"Specimen_Class\", Specimen.createdOn as \"Created_On\", Specimen.initialQty as \"Initial_Quantity\", Specimen.availableQty as \"Available_Quantity\", Specimen.concentration, Specimen.collectionStatus as \"Collection_Status\", Specimen.activityStatus as \"Activity_Status\", Specimen.availabilityStatus as \"Availability_Status\", Specimen.comments as \"Comments\", Specimen.creationTime as \"Creation_Time\", Specimen.updateTime as \"Update_Time\", CollectionProtocol.shortTitle as \"Collection_Protocol_ShortTitle\", CollectionProtocol.Title as \"Collection_Protocol_Title\" where  CollectionProtocol.id exists   limit 0, 10000",
    "wideRowMode": "DEEP"
}

result = api.execute_query_as_dataframe(query)
print(result)
