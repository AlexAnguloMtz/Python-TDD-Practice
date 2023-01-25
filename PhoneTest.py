from Phone import Phone

class PhoneTest(unittest.TestCase):
    
    def test_should_parse_phone_prefix(self):
        phone = Phone('+52-6622778899-78')
        self.assertEqual('+52', phone.prefix)
        
    def test_should_parse_phone_value(self):
        phone = Phone('+52-6622778899-78')
        self.assertEqual('6622778899', phone.value)
        
    def test_should_parse_phone_extension(self):
        phone = Phone('+52-6622778899-78')
        self.assertEqual('78', phone.extension)
        
if __name__ == '__main__':
    unittest.main()