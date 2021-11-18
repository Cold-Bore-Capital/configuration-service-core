from unittest import TestCase
from config_service.core import Core, MissingEnviron, ErrorFlagTrue
import os

class TestCore(TestCase):


    def test__load_env(self):

        # set an env to work with.

        os.environ['TEST_ME_X'] = '1'

        c = Core()

        # Test simple recall.
        res = c._load_env('TEST_ME_X')
        self.assertEqual('1', res)

        # Test assigned value where no value assigned
        res = c._load_env('TEST_ME_X',
                          assigned_value=None)
        self.assertEqual('1', res)

        # Test when assigned value override is set
        res = c._load_env('TEST_ME_X',
                          assigned_value='2')
        self.assertEqual('2', res)

        # Test default value
        res = c._load_env('THIS_DOESNT_EXIST',
                          default_value='A')
        self.assertEqual('A', res)

        # Test test mode responses section.
        ######### TEST MODES ############
        c._test_mode = True
        # Test simple recall.
        res = c._load_env('TEST_ME_X', test_response='test_res')
        self.assertEqual('test_res', res)

        # Test assigned value where no value assigned
        res = c._load_env('TEST_ME_X',
                          assigned_value=None,
                          test_response='test_res')
        self.assertEqual('test_res', res)
        c._test_mode = False
        ######### End Test Mode Section ############


        ######## Check error states. ############

        with self.assertRaises(MissingEnviron) as e:
            res = c._load_env('THIS_DOESNT_EXIST', error_flag=True)

        with self.assertRaises(ErrorFlagTrue) as e:
            res = c._load_env('THIS_DOESNT_EXIST', error_flag=True, default_value='1')

