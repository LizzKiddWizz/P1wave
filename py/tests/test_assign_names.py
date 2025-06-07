import unittest
from py.utils.assign_names import assign_names

class TestAssignNames(unittest.TestCase):

    def test_assign_names_to_unnamed_components(self):
        mock_page = {
            'form': {
                'items': [
                    {'type': 'text'},
                    {'type': 'text', 'name': 'username'},
                    {'type': 'button'}
                ]
            },
            'dialog': {
                'items': [
                    {'type': 'dropdown'},
                    {'type': 'button'}
                ]
            }
        }

        assign_names(mock_page)

        self.assertEqual(mock_page['form']['items'][0]['name'], 'auto_item_1')
        self.assertEqual(mock_page['form']['items'][1]['name'], 'username')  # should remain unchanged
        self.assertEqual(mock_page['form']['items'][2]['name'], 'auto_item_2')
        self.assertEqual(mock_page['dialog']['items'][0]['name'], 'auto_item_3')
        self.assertEqual(mock_page['dialog']['items'][1]['name'], 'auto_item_4')

if __name__ == '__main__':
    unittest.main()
