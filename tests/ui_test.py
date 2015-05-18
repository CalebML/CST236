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
        if( self.app.sharpTona['Teach'].IsEnabled() ):
            error = 'Teach is enabled'
        if( self.app.sharpTona['Correct'].IsEnabled() ):
            error = 'Correct is enabled'
        if( self.app.sharpTona['Answer:Edit'].IsEnabled() ):
            error = 'Answer box is enabled'
        
        if( error ):
            print error
        self.assertTrue(error == None)

    def test_ask_question(self):
        error = None
        self.app.sharpTona['Question:Edit'].TypeKeys('What is the answer to everything?', with_spaces=True)
        self.app.sharpTona['Ask'].Click()

        if( self.app.sharpTona['Answer:Edit'].Texts()[0] != '42' ):
            error = 'Answer is not 42'
        if( not self.app.sharpTona['Answer:Edit'].IsEnabled() ):
            error = 'Answer box is not enabled after asking valid question'
            
        self.app.sharpTona['Answer:Edit'].TypeKeys('42.0', with_spaces=True)
        self.app.sharpTona['Correct'].Click()

        if( self.app.sharpTona['Teach'].IsEnabled() ):
            error = 'Teach is enabled'
        if( self.app.sharpTona['Correct'].IsEnabled() ):
            error = 'Correct is enabled'
        if( self.app.sharpTona['Answer:Edit'].IsEnabled() ):
            error = 'Answer box is enabled'

        self.app.sharpTona['Ask'].Click()

        if( self.app.sharpTona['Answer:Edit'].Texts()[0] != '42.0' ):
            error = 'Answer is not 42.0'
            
        if( error ):
            print error
        self.assertTrue(error == None)

    def test_no_question(self):
        error = None
        self.app.sharpTona['Ask'].Click()

        if( self.app.sharpTona['Answer:Edit'].Texts()[0] != 'Was that a question?' ):
            error = 'Seeing a quesrion when there is none'

        if( error ):
            print error
        self.assertTrue(error == None)

    def test_Unknown_question(self):
        error = None
        self.app.sharpTona['Question:Edit'].TypeKeys('Who is Iron Man?', with_spaces=True)
        self.app.sharpTona['Ask'].Click()

        if( self.app.sharpTona['Answer:Edit'].Texts()[0] != 'I don\'t know please teach me.' ):
            error = 'System reconizing unknown questions'
        
        if( not self.app.sharpTona['Teach'].IsEnabled() ):
            error = 'Teach is not enabled'

        self.app.sharpTona['Answer:Edit'].TypeKeys('Tony Stark', with_spaces=True)
        self.app.sharpTona['Teach'].Click()

        if( self.app.sharpTona['Teach'].IsEnabled() ):
            error = 'Teach is enabled'
        if( self.app.sharpTona['Correct'].IsEnabled() ):
            error = 'Correct is enabled'
        if( self.app.sharpTona['Answer:Edit'].IsEnabled() ):
            error = 'Answer box is enabled'

        self.app.sharpTona['Ask'].Click()

        if( self.app.sharpTona['Answer:Edit'].Texts()[0] != 'Tony Stark' ):
            error = 'System not saving taught answers'

        if( error ):
            print error
        self.assertTrue(error == None)

        
