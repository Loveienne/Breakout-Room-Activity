'''

import unittest
from app import app, db, User, Project
from flask_login import current_user

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        self.client = app.test_client()
        with app.app_context():
            db.create_all()
    
    def test_login(self):
        response = self.client.post('/login', json={
            'email': 'test@test.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
    
    def test_project_search(self):
        response = self.client.get('/projects?search=test')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
    
    def test_add_collaborator(self):
        response = self.client.post('/project/1/collaborate', 
            json={'email': 'collaborator@test.com'})
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        with app.app_context():
            db.drop_all()

if __name__ == '__main__':
    unittest.main()


'''