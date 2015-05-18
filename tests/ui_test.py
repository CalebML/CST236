#import pywinauto
from pywinauto import application
from unittest import TestCase


class testUI(TestCase):
    def setUp(self):
        self.app = application.Application()
        self.app.start_('SharpTona.exe')

    def tearDown(self):
        self.app.sharpTona.Close()

    def test_label_and_initial_state(self):
        error = None
        if( self.app.window_().Texts()[0] != 'SharpTona' ):
            error = 'SharpTona is not the title'
            print self.app.window_().Texts()[0]
        if( self.app.sharpTona['Question'].Texts()[0] != 'Question:' ):
            error = 'There is no Question label'
            print self.app.sharpTona['Question'].Texts()[0]
        if( self.app.sharpTona['Answer'].Texts()[0] != 'Answer: ' ):
            error = 'There is no Answer label'
            print self.app.sharpTona['Answer'].Texts()[0]
        
        if( error ):
            print error
        self.assertTrue(error == None)

