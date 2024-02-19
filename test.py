'''
Created object for testing purposes
'''


class Test:
    '''
    Test object for testing purposes
    '''

    id = None
    name = ''
    num = None

    def __init__(self, test_id: int = None, name: str = None,
                 num: int = None) -> None:
        self.id = test_id
        self.name = name
        self.num = num

    def set_id(self, test_id: int):
        '''
        Set test identification
        '''
        self.id = test_id

        return self

    def get_id(self) -> int | None:
        '''
        Returns test identification
        '''
        return self.id

    def set_name(self, test_name: str):
        '''
        Set test name
        '''
        self.name = test_name

        return self

    def get_name(self) -> int | None:
        '''
        Returns test name
        '''
        return self.name

    def set_num(self, test_num: int):
        '''
        Sets test num
        '''
        self.num = test_num

        return self

    def get_num(self) -> int | None:
        '''
        Returns test num
        '''
        return self.num
