''' Needed libraries'''

import requests
import pandas as pd


def extract_sp_hist_record (species,token):

    '''This function get an species IUCN historical records from its API
        A IUCN token is needed to be defined'''
    species_split = species.split()
    gen = species_split[0]
    sp = species_split[-1]

    url_sp = f"https://apiv3.iucnredlist.org/api/v3/species/history/name/{gen}%20{sp}?token={token}"
    get_sp = requests.get(url_sp)
    info_sp = get_sp.json()
    sp_df = pd.DataFrame.from_dict(info_sp.get("result"))

    
    return sp_df



