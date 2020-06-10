import unittest
from tests.test_1_sing_up import SignUpTest
from tests.test_2_login import LoginTest
from tests.test_3_create_review import CreateReviewTest
from tests.test_4_delete_review import DeleteReviewTest
from tests.test_5_delete_account import DeleteAccountTest

sing_up = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
create = unittest.TestLoader().loadTestsFromTestCase(CreateReviewTest)
remove = unittest.TestLoader().loadTestsFromTestCase(DeleteReviewTest)
delete = unittest.TestLoader().loadTestsFromTestCase(DeleteAccountTest)

regression_test = unittest.TestSuite([sing_up, login, create, remove, delete])

unittest.TextTestRunner(verbosity=2).run(regression_test)

