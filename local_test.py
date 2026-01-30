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
    "aql": "select CollectionProtocol.id, CollectionProtocol.Title, CollectionProtocol.catalogId, Participant.participantId, Participant.dateOfBirth, Participant.gender, Participant.customFields.ucch_participant_custom_fields.beispielinfo as \"UCCH_Info\", SpecimenCollectionGroup.id, SpecimenCollectionGroup.clinicalDiagnoses.value, SpecimenCollectionGroup.clinicalDiagnoses.code, Specimen.id, Specimen.label, Specimen.type, Specimen.tissueSite, Specimen.tissueSide, Specimen.pathologicalStatus, Specimen.createdOn, Specimen.initialQty, Specimen.id as \"$specimenId\", CollectionProtocol.id as \"$cpId\" where CollectionProtocol.id any and Participant.participantId any and Participant.gender any and Specimen.id any   limit 0, 1000 ",
    "wideRowMode": "DEEP"
}

result = api.execute_query_as_dataframe(query)
print(result)
