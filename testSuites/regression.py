import unittest
from tests.sing_up_test import SignUpTest
from tests.login_test import LoginTest
from tests.create_review_test import CreateReviewTest
from tests.delete_review_test import DeleteReviewTest
from tests.delete_account_test import DeleteAccountTest

sing_up = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
create = unittest.TestLoader().loadTestsFromTestCase(CreateReviewTest)
remove = unittest.TestLoader().loadTestsFromTestCase(DeleteReviewTest)
delete = unittest.TestLoader().loadTestsFromTestCase(DeleteAccountTest)

regression_test = unittest.TestSuite([sing_up, login, create, remove, delete])

unittest.TextTestRunner(verbosity=2).run(regression_test)

