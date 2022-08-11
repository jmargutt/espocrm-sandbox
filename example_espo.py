from espo_api_client import EspoAPI, EspoAPIError

# create a client to EspoCRM
espo_client = EspoAPI(url='https://espo.redcross.org.ua', api_key='...')

# get all cases
case_list = espo_client.request('GET', 'Case')['list']

# get a specific case based on id
params = {
    "select": "id,name,firstNameEspo,lastNameEspo,patronymicNameEspo,sexEspo,ageEspo,emailEspo,phoneEspo,"
              "regionEspo,addressEspo,messengersEspo,otherVulnerabilities,tutelage,providesConstantCare,"
              "disabilityGroup,additionalVulnerability,isCaseProcessedContactUpdate,cases",
    "where": [
        {
            "type": "equals",
            "attribute": "number",
            "value": "7812"
        }
    ]
}
case_7812 = espo_client.request('GET', 'Case', params)['list']

# check if a contact already exists
params = {
    "select": "id",
    "where": [
        {
            "type": "contains",
            "attribute": "phoneNumber",
            "value": "123456"
        },
    ]
}
contact_id_list = espo_client.request('GET', 'Contact', params)['list']
if len(contact_id_list) == 0:
    # if contact doesn't exist, create contact
    payload = {
        'firstName': "...",
        'lastName': "...",
        'patronymicName': "...",
        'sex': "...",
        'age': "...",
        'phoneNumber': "...",
        '...': '...',
        'skipDuplicateCheck': True
    }  # payload contains the data of the contact
    try:
        result = espo_client.request('POST', 'Contact', payload)
        contact_id = result['id']
    except EspoAPIError as e:
        print(e)
        print("POST Contact")
        print(payload)