# test.py
"""
from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

sample_playlist_id = ObjectId('')
sample_playlist = {
    'name': 'Mr. Chew',
    'breed': 'poodle'
    'description': 'He is a cute dog, but is a handful.',
    'price': '150',
    'img_url': [

    ]
}

sample_form_data = {
    'name': sample_adoption['name'],
    'breed': sample_adoption['breed'],
    'description': sample_adoption['description'],
    'price': sample_adoption['price'],
    'img_url': sample_adoption['img_url']
}

class PlaylistsTests(TestCase):
    Flask tests.

    def setUp(self):
        Stuff to do before every test.
        
        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
    
    def test_index(self):
        Test the adoptions homepage.
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Adoption', result.data)
    
    def test_new(self):
        Test the new adoption creation page.
        result = self.client.get('/adoptions/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Adoption Ad', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_adoption(self, mock_find):
        Test showing a single adoption ad.
        mock_find.return_value = sample_playlist

        result = self.client.get(f'/adoptions/{sample_adoption_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Mr. Chew', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_adoption(self, mock_find):
        Test editing a single adoption ad.
        mock_find.return_value = sample_adoption

        result = self.client.get(f'/adoptions/{sample_adoption_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Mr. Chew', result.data)

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_submit_adoption(self, mock_insert):
        Test submitting a new adoption ad.
        result = self.client.post('/adoptions', data=sample_form_data)

        # After submitting, should redirect to that adoption ad's page
        self.assertEqual(result.status, '302 FOUND')
        mock_insert.assert_called_with(sample_adoption)

    @mock.patch('pymongo.collection.Collection.update_one')
    def test_update_adoption(self, mock_update):
        result = self.client.post(f'/adoptions/{sample_adoption_id}',
                                  data=sample_form_data)

        self.assertEqual(result.status, '302 FOUND')
        mock_update.assert_called_with({'_id': sample_adoption_id},
                                       {'$set': sample_adoption})

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_adoption(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/adoptions/{sample_adoption_id}/delete',
                                  data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_adoption_id})

if __name__ == '__main__':
    unittest_main()
"""