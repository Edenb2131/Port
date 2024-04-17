import requests

CLIENT_ID = 'WL92dw5KSobwoBwLOa7UTgMob8gBgB8G'
CLIENT_SECRET = 'lBbnVGRDRejTA3p0yLrHEYxROSuSaheqvJORZPj2duPkDruIIsqpo6fN273oFx4o'

API_URL = 'https://api.getport.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)

access_token = token_response.json()['accessToken']
# You can now use the value in access_token when making further requests


# get all the blueprints. GET v1/blueprints
response_blueprints = requests.get(f'{API_URL}/blueprints', headers={'Authorization': f'Bearer {access_token}'})
# print(response_blueprints.json())

# get number of all blueprints
number_of_blueprints = len(response_blueprints.json()['blueprints'])

# get all the enteties. /v1/blueprints/{blueprint_identifier}/entities
for i in range(number_of_blueprints):
    blueprint_identifier = response_blueprints.json()['blueprints'][i]
    identefier = blueprint_identifier['identifier']
    response_entities = requests.get(f'{API_URL}/blueprints/{identefier}/entities',
                                     headers={'Authorization': f'Bearer {access_token}'})

    entities = response_entities.json()['entities']

    for entity in entities:
        # get all the properties into a list
        properties = entity['properties']

        # I will skip all the interations that are not service for now
        if blueprint_identifier['identifier'] != 'service':
            continue

        # get all the service_framework into a list
        try:
            service_framework = entity['relations']['service_framework']

        except:
            service_framework = []

        num_of_eols = 0

        # check if the service_framework is empty and skip the iteration if it is
        if len(service_framework) == 0:
            # print(f"No service_framework found for {entity['title']} Skipping iteration.")
            continue

        # get the number of EOLs
        for j in range(len(service_framework)):

            # make an API call to /v1/blueprints/{blueprint_identifier}/entities/{entity_identifier}
            response_entity = requests.get(f'{API_URL}/blueprints/framework/entities/{service_framework[j]}',
                                           headers={'Authorization': f'Bearer {access_token}'})
            # If property: state = "EOL" then increment the number of EOLs
            if response_entity.json()['entity']['properties']['state'] == 'EOL':
                num_of_eols += 1

        # print the number of EOLs
        print(f'Number of EOLs: {num_of_eols} for {entity["title"]}')
        entity['properties']['num_of_eols_pack'] = num_of_eols # update the number of EOLs to the entity
        entity['icon'] = 'None' # had to make this change because the icon was not in a string format!

        # update the number of EOLs to the service
        response_service = requests.put(f'{API_URL}/blueprints/{identefier}/entities/{entity["identifier"]}',
                                        headers={'Authorization': f'Bearer {access_token}'}, json=entity)
        # print(response_service.json())


    

