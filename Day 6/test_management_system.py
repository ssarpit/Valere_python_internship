import unittest
from employee_management_system import Employee, Manager, Developer


class TestEmployeeSystem(unittest.TestCase):
    def test_employee(self):
        emp = Employee('aj', 101, 50000, 22)
        self.assertEqual(emp.name, 'aj')
        self.assertEqual(emp.emp_id, 101)
        self.assertEqual(emp.salary, 50000)
        self.assertEqual(emp.age, 22)

    def test_manager(self):
        mgr = Manager('Arpit', 102, 56000, 22, 'AIML')
        self.assertEqual(mgr.name, 'Arpit')
        self.assertEqual(mgr.emp_id, 102)
        self.assertEqual(mgr.salary, 56000)
        self.assertEqual(mgr.age, 22)
        self.assertEqual(mgr.department, 'AIML')

    def test_developer(self):
        dev = Developer('aj', 103, 52000, 22, 'python')
        self.assertEqual(dev.name, 'aj')
        self.assertEqual(dev.emp_id, 103)
        self.assertEqual(dev.salary, 52000)
        self.assertEqual(dev.age, 22)
        self.assertEqual(dev.tech_stack, 'python')


if __name__ == '__main__':
    unittest.main()
