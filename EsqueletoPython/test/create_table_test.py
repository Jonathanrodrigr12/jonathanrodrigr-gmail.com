import unittest
import os.path
from app.services.region_all_service import RegionAllService
from app.infrastructure.context.mongo import MongoDBContext

class TestCreateTable(unittest.TestCase):
    def setUp(self):
        self.region = RegionAllService()
        self.mongo = MongoDBContext()
    
    def test_create_file_not(self):
        file = os.path.exists('./data/data.json')
        print("El archvio Existe:"+ str(file))
        self.assertEqual(file, False)
    def test_create_table(self):
        self.region.create_region()
        self.assertEqual(True, True)

    def test_validation_file_create(self):
        file = os.path.exists('./data/data.json')
        print("El archvio Existe:"+ str(file))
        self.assertEqual(file, True)    