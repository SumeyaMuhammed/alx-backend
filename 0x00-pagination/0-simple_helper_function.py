#!/usr/bin/env python3

'''
    simple pagination py code
'''

def index_range(page, page_size):
    '''
    This function returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
    '''
    return (page_size * (page - 1), page_size * page )
