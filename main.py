import json
import requests
import re
import polymorph_common

'''
http://polymorph.weigelworld.org/cgi-bin/webapp.cgi?page=generic_region_search&plugin=retrieve_hdr&project=MPICao2010&rm=compute&accessions_list1=Agu-1&accessions_list1=Bak-2&accessions_list1=Bak-7&accessions_list1=Cdm-0&accessions_list1=Del-10&accessions_list1=Dog-4&accessions_list1=Don-0&accessions_list1=Ey15-2&accessions_list1=Fei-0&accessions_list1=HKT2.4&accessions_list1=ICE1&accessions_list1=ICE102&accessions_list1=ICE104&accessions_list1=ICE106&tair_id=At4g25530&download=csv
'''

def search(arg):
    
    # Extract query parameters
    # Detect whether client is searching by locus or position
    search_mode = 0
    '''
    if arg['locus']:
        Todo: Validate locus via regex
        locus = arg['locus']
        search_mode = 1 # by locus
    elif arg['chromosome']:
        # Todo: Validate chromosome
        chrom = arg['chromosome']
        start_position = arg['start']
        stop_postiion = arg['stop']    
        search_mode = 2 # by position
    '''
    # Todo: Extract and validate accessions against known list 
    # Todo: Accept and validate project ID
    
    payload = {'page': 'generic_region_search', 'plugin': 'retrieve_hdr', 'project': 'MPICao2010', 'rm': 'compute', 'accessions_list1': ['Agu-1', 'Bak-2', 'Bak-7', 'Cdm-0', 'Del-10', 'Dog-4', 'Don-0', 'Ey15-2', 'Fei-0', 'HKT2.4', 'ICE1', 'ICE102', 'ICE104', 'ICE106'], 'download': 'csv', 'tair_id': 'At4g25530'}
    r = requests.get(polymorph_common.base_url(), params=payload)
    print(r.url)
    
    # Todo: Fetch results, return as AIP feature objects, which are convertible to GFF
    # Todo: Speak with @waltermoreira about composition of services - I think we have
    #       our first use case. Conversion of AIP feature objects to GFF on the fly
    
    pass

def list(arg):
    pass
