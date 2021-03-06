# _*_ coding:utf-8 _*_
import unittest
import requests

# 登录
def get_session():
    req = requests.sessions()
    url = ""
    data = {}
    req.post(url,data,verify=False)
    return req

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
    inherit from this class.
    """

    def __init__(self,methodName="runTest",param=None):
        super(ParametrizedTestCase,self).__init__(methodName)

    @classmethod
    def setUpclass(cls):
        # cls.rq = get_session() # 登录后的session
        pass

    @classmethod
    def tearDown(cls):
        pass

    @staticmethod
    def parametrize(testcase_klass,param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name,param=param))
        return suite