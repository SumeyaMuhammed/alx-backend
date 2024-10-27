#!/usr/bin/env python3
'''
 Simple pagination
'''

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(page, page_size):
        return (page_size * (page - 1), page_size * page )

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        function to varify that both arguments are integers greater than 0 and paginate and return the appropriate page of the dataset. 
        '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]

