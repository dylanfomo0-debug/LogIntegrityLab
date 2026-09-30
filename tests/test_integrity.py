import unittest
from src.generate_logs import normal_events, tamper
from src.detect_tampering import check

class IntegrityTests(unittest.TestCase):
    def test_normal_log_is_clean(self): self.assertEqual(check(normal_events()), [])
    def test_duplicate_is_found(self): self.assertTrue(check(tamper(normal_events(), "duplicate")))
    def test_unknown_user_is_found(self): self.assertTrue(check(tamper(normal_events(), "invalid_user")))
    def test_new_ip_is_found(self): self.assertTrue(check(tamper(normal_events(), "new_ip")))

if __name__ == "__main__": unittest.main()
