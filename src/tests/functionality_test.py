import unittest
import os, sys

dir = os.path.dirname("playlist_functionality.py")
sys.path.append(dir)
from application.playlist_functionality import Playlist_Gen

class TestButton(unittest.TestCase):

    def setUp(self):
        self.func = Playlist_Gen()

    def test_initialization_correct(self):
        self.assertEqual(self.func.username, "21as4yvrgnnnjpzb7qqbcoyva")
        self.assertEqual(self.func.scope, "playlist-modify-public")
        self.token = None
        self.spotifyObject = None
    
