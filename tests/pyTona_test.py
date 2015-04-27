"""
Test for pyTona
"""
import getpass
import datetime
from pyTona.main import Interface
from ReqTracer import requirements#, Requirements
from unittest import TestCase


class testInterface(TestCase):
    def setUp(self):
        self.obj = Interface()

    def test__init__(self):
        self.assertEqual(self.obj.last_question, None)

        """
        test who, what, where, when, why, and how
        """
    @requirements(['#0001', '#0002', '#0009'])
    def test_string_what(self):
        answer = self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3E) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0009'])
    def test_string_how(self):
        answer = self.obj.ask('How are you' + chr(0x3E) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0009'])
    def test_string_where(self):
        answer = self.obj.ask('Where am i' + chr(0x3E) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0009'])
    def test_string_why(self):
        answer = self.obj.ask('Why is this a question' + chr(0x3E) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0009'])
    def test_string_Who(self):
        answer = self.obj.ask('Who are you' + chr(0x3E) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')
        """
        end test who, what, where, when, why, and how
        """

    #Determining Answers reqs
    
    @requirements(['#0001', '#0003'])
    def test_no_valid_keyword(self):
        answer = self.obj.ask('are you okay' + chr(0x3E) )
        self.assertEqual(answer, 'Was that a question?')

    @requirements(['#0001', '#0004'])
    def test_no_question_mark(self):
        answer = self.obj.ask('are you okay' + chr(0x3E) )
        self.assertEqual(answer, 'Was that a question?')

    @requirements(['#0001', '#0002', '#0007', '#0008'])
    def test_pass_number_to_func(self):
        answer = self.obj.ask('What is 10560 feet in miles' + chr(0x3E) )
        self.assertEqual(answer, '2.0')
        
    #Providing Answers reqs

    @requirements(['#0001', '#0002', '#0005', '#0006', '#0008', '#0010', '#0011'])
    def test_niney_pct_match(self):
        self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3E) )
        self.obj.teach('42')
        answer = self.obj.ask('What is the meaning of life according to Douglas' + chr(0x3E) )
        self.assertEqual(answer, '42')    

    @requirements(['#0001', '#0012'])
    def test_no_question(self):
        answer = self.obj.teach('42')
        self.assertEqual(answer, 'Please ask a question first')

    @requirements(['#0001', '#0013'])
    def test_teaching_twice(self):
        self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3E) )
        self.obj.teach('42')
        #self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3E) )
        response = self.obj.teach('There is no answer')
        answer = self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3E) )
        self.assertTrue(
            (response == 'I don\'t know about that. I was taught differently') &
            (answer == '42') )

    #Correcting Answers reqs

    @requirements(['#0001', '#0014', '#0015'])
    def test_correcting(self):
        self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3E) )
        self.obj.teach('48')
        self.obj.correct('42')
        answer = self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3E) )
        self.assertEqual(answer, '42')

    @requirements(['#0001', '#0014', '#0016'])
    def test_correcting_before_asking(self):
        reponse = self.obj.correct('42')
        self.assertEqual(reponse, 'Please ask a question first')

    #Initial Answers Provided reqs

    @requirements(['#0001', '#0002', '#0005', '#0008', '#0017'])
    def test_ft_in_miles_question(self):
        answer = self.obj.ask('What is 10560 feet in miles' + chr(0x3E) )
        self.assertEqual(answer, '2.0 miles' )

    @requirements(['#0001', '#0002', '#0005', '#0008', '#0018'])
    def test_sec_since_time_question(self):
        t = datetime.time(1, 30)
        answer = self.obj.ask('How many seconds since ' + format(t) + chr(0x3E) )
        now = datetime.datetime.now()
        sec = ( ( (now.hour * 60) + now.minute ) * 60 ) + now.second
        tSec =  ( ( (t.hour * 60) + t.minute ) * 60 ) + t.second
        sec = sec - tSec
        self.assertEqual(answer, str(sec) + ' seconds' )

    @requirements(['#0001', '#0002', '#0008', '#0019'])
    def test_who_invented_python_question(self):
        answer = self.obj.ask('Who invented Python' + chr(0x3E) )
        self.assertEqual(answer, 'Guido Rossum(BFDL)' )

    @requirements(['#0001', '#0002', '#0008', '#0020'])
    def test_why_dont_you_understand_question(self):
        answer = self.obj.ask('Why don\'t you understand me' + chr(0x3E) )
        self.assertEqual(answer, 'Because you do not speak 1s and 0s' )

    @requirements(['#0002', '#0001', '#0008', '#0021'])
    def test_shutdown_question(self):
        answer = self.obj.ask('Why don\'t you shutdown' + chr(0x3E) )
        self.assertEqual(answer, 'I\'m afraid I can\'t do that ' + format(getpass.getuser()) )
