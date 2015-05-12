"""
Test for pyTona
"""
import getpass
import datetime
import time
import socket
import subprocess
import threading
from pyTona.main import Interface
import pyTona.main
from ReqTracer import requirements
from pyTona.question_answer import QA
from unittest import TestCase
from mock import Mock
from mock import MagicMock
from mock import patch
#from pyTona.answer_funcs import get_hdd_access_time

class testInterface(TestCase):
    def setUp(self):
        self.obj = Interface()
        
    
    def tearDown(self):
        if pyTona.answer_funcs.seq_finder is not None:
            pyTona.answer_funcs.seq_finder.stop()
            pyTona.answer_funcs.seq_finder = None
            
        if pyTona.answer_funcs.prime_finder is not None:
            pyTona.answer_funcs.prime_finder.stop()
            pyTona.answer_funcs.prime_finder = None
    
    
    def test__init__(self):
        self.assertEqual(self.obj.last_question, None)

        """
        test who, what, where, when, why, and how
        """
    @requirements(['#0001', '#0002', '#0009'])
    def test_string_what(self):
        answer = self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3F) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0009'])
    def test_string_how(self):
        answer = self.obj.ask('How are you' + chr(0x3F) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0009'])
    def test_string_where(self):
        answer = self.obj.ask('Where are we going' + chr(0x3F) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0009'])
    def test_string_why(self):
        answer = self.obj.ask('Why is this a question' + chr(0x3F) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0009'])
    def test_string_Who(self):
        answer = self.obj.ask('Who are you' + chr(0x3F) )
        self.assertEqual(answer, 'I don\'t know, please provide the answer')
        """
        end test who, what, where, when, why, and how
        """

    #Determining Answers reqs
    
    @requirements(['#0001', '#0003'])
    def test_no_valid_keyword(self):
        answer = self.obj.ask('are you okay' + chr(0x3F) )
        self.assertEqual(answer, 'Was that a question?')

    @requirements(['#0001', '#0004'])
    def test_no_question_mark(self):
        answer = self.obj.ask('are you okay' + chr(0x3F) )
        self.assertEqual(answer, 'Was that a question?')

    @requirements(['#0001', '#0002', '#0007', '#0008'])
    def test_pass_number_to_func(self):
        answer = self.obj.ask('What is 10560 feet in miles' + chr(0x3F) )
        self.assertEqual(answer, '2.0 miles')
        
    #Providing Answers reqs

    @requirements(['#0001', '#0002', '#0005', '#0006', '#0008', '#0010', '#0011'])
    def test_niney_pct_match(self):
        self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3F) )
        self.obj.teach('42')
        answer = self.obj.ask('What is the meaning of life according to Douglas' + chr(0x3F) )
        self.assertEqual(answer, '42')    

    @requirements(['#0001', '#0012'])
    def test_no_question(self):
        answer = self.obj.teach('42')
        self.assertEqual(answer, 'Please ask a question first')

    @requirements(['#0001', '#0013'])
    def test_teaching_twice(self):
        self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3F) )
        self.obj.teach('42')
        #self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3F) )
        response = self.obj.teach('There is no answer')
        answer = self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3F) )
        self.assertTrue(
            (response == 'I don\'t know about that. I was taught differently') &
            (answer == '42') )

    #Correcting Answers reqs

    @requirements(['#0001', '#0014', '#0015'])
    def test_correcting(self):
        self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3F) )
        self.obj.teach('48')
        self.obj.correct('42')
        answer = self.obj.ask('What is the meaning of life according to Douglas adams' + chr(0x3F) )
        self.assertEqual(answer, '42')

    @requirements(['#0001', '#0014', '#0016'])
    def test_correcting_before_asking(self):
        reponse = self.obj.correct('42')
        self.assertEqual(reponse, 'Please ask a question first')

    #Initial Answers Provided reqs

    @requirements(['#0001', '#0002', '#0005', '#0008', '#0017'])
    def test_ft_in_miles_question(self):
        answer = self.obj.ask('What is 10560 feet in miles' + chr(0x3F) )
        self.assertEqual(answer, '2.0 miles' )
    """
    #requirement removed
    @requirements(['#0001', '#0002', '#0005', '#0008', '#0018'])
    def test_sec_since_time_question(self):
        t = datetime.time(1, 30)
        answer = self.obj.ask('How many seconds since ' + format(t) + chr(0x3F) )
        now = datetime.datetime.now()
        sec = ( ( (now.hour * 60) + now.minute ) * 60 ) + now.second
        tSec =  ( ( (t.hour * 60) + t.minute ) * 60 ) + t.second
        sec = sec - tSec
        self.assertEqual(answer, str(sec) + ' seconds' )
    """
    @requirements(['#0001', '#0002', '#0008', '#0019'])
    def test_who_invented_python_question(self):
        answer = self.obj.ask('Who invented Python' + chr(0x3F) )
        self.assertEqual(answer, 'Guido Rossum(BDFL)' )

    @requirements(['#0001', '#0002', '#0008', '#0020'])
    def test_why_dont_you_understand_question(self):
        answer = self.obj.ask('Why don\'t you understand me' + chr(0x3F) )
        self.assertEqual(answer, 'Because you do not speak 1s and 0s' )

    @requirements(['#0002', '#0001', '#0008', '#0021'])
    def test_shutdown_question(self):
        answer = self.obj.ask('Why don\'t you shutdown' + chr(0x3F) )
        self.assertEqual(answer, 'I\'m afraid I can\'t do that ' + format(getpass.getuser()) )

    @requirements(['#0022'])
    def test_get_git_name(self):
        try:
            process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
            output = process.communicate()[0]
            val = output.strip()
        except:
            val = "Unknown"
        answer = self.obj.ask('Where am i?')
        self.assertEqual(answer, val)

    @requirements(['#0023'])
    def test_get_git_url(self):
        try:
            process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
            output = process.communicate()[0]
            val = output.strip()
        except:
            val = 'Unknown'
        answer = self.obj.ask('Where are you?')
        self.assertEqual(answer, val)
    
    @requirements(['#0028'])
    def test_get_fib_number(self):       
        self.obj.ask('What is the 2 digit of the Fibonacci sequence?')
        time.sleep(0.2)
        answer = self.obj.ask('What is the 5 digit of the Fibonacci sequence?')
        self.assertEqual(answer, 5)
        
    
    @requirements(['#0029'])
    def test_fib_thinking(self):        
        count = 100
        answer = []
        while(count > 0):    #call it 100 times
            answer.append( self.obj.ask('What is the 47 digit of the Fibonacci sequence?') )
            count -= 1

        count = 0           #see how many times it gave each answer
        thinking = 0
        oneSecond = 0
        coolYourJets = 0
        while(count < 100):
            if(answer[count] == 'Thinking...'):
                thinking +=1
            elif(answer[count] == 'One second'):
                oneSecond +=1
            elif(answer[count] == 'cool your jets'):
                coolYourJets +=1
            count +=1
        print thinking
        print oneSecond
        print coolYourJets
        self.assertTrue( (thinking <= 75) &
                         (thinking >= 45) &
                         (oneSecond <= 45) &
                         (oneSecond >= 15) &
                         (coolYourJets <= 25) &
                         (coolYourJets >= 0) )
    
    @requirements(['#0024', '#0025', '#0026'])
    def test_get_users(self):        
        with patch.object(socket, 'socket') as mock_s:
            mock_s.return_value.connect.return_value = True
            mock_s.return_value.recv.return_value = 'user1$user2'
            answer = self.obj.ask('Who else is here?')
        
        self.assertEqual(answer, ['user1', 'user2'])

    @requirements(['#0027'])
    def test_no_connection_to_server(self):        
        with patch.object(socket.socket, 'connect') as mock_s:
            #mock_s.return_value.connect.return_value = False
            #mock_s.return_value.recv.return_value = ''
            answer = self.obj.ask('Who else is here?')
        
        self.assertEqual(answer, 'IT\'S A TRAAAPPPP')

    @requirements(['#0031'])
    def test_store_answer_under_5ms(self):
        self.obj.ask('What is the meaning of life according to Douglas adams?')
        t0 = time.clock()
        self.obj.teach('42')
        t1 = time.clock() - t0
        print t1
        self.assertLess(t1, 0.005)

    @requirements(['#0032'])
    def test_retrieve_answer_under_5ms(self): 
        self.obj.ask('What is the meaning of life according to Douglas adams?')
        self.obj.teach('42')
        t0 = time.clock()
        self.obj.ask('What is the meaning of life according to Douglas adams?')
        t1 = time.clock() - t0
        self.assertLess(t1, 0.005)
    
    @requirements(['#0033', '#0034'])
    def test_stop_after_1000_fib_seq(self): 
        self.obj.ask('What is the 1000 digit of the Fibonacci sequence?')      # start fib seq
        
        t0fib = time.clock()
        t1fib = 0
        while( (pyTona.answer_funcs.seq_finder.num_indexes < 1000) & (t1fib < 60) ):
            t1fib = time.clock() - t0fib
            #time.sleep(0.1)
        time.sleep(0.1) #give it time to calculare past 1000
        self.obj.ask('What is the 1001 digit of the Fibonacci sequence?')
        print t1fib
        self.assertEqual(pyTona.answer_funcs.seq_finder.num_indexes, 1000)
    
    @requirements(['#0030', '#0032'])
    def test_1_mil_questions(self): 
        numQuestions = 9
        i = 1
        addedOneMil = True
        
        t0 = time.clock()
        while(numQuestions < 999999):
            """                  # This method takes 5.9 sec to add 1,000 questions
            numQuestions = numQuestions + 1
            i = i + 1
            question = 'What a' + str(i) + '?'
            answer = self.obj.ask( question )
            retVal = self.obj.teach(str(i))
            if( (retVal != None) ):
                #print question
                #print i
                #print numQuestions
                #print answer
                #print retVal
                numQuestions = 1000000
                addedOneMil = False
            """                  # This method takes 0.003 seconds to add 1,000 questions
            question = 'What a' + str(i) + '?'
            self.obj.question_answers[question] = QA(question, str(i))
            
            numQuestions = numQuestions + 1
            i = i + 1
        
        # 999,999 questions and answers are in the system now
        self.obj.ask( 'How can the system hold 1,000,000 questions?' )
        self.obj.teach('Using a dictionary!')
        
        # check 1,000,000th answer
        t2 = time.clock()
        answer = self.obj.ask( 'How can the system hold 1,000,000 questions?' )
        t3 = time.clock() - t2
        if(answer != 'Using a dictionary!'):
            addedOneMil = False
        
        t1 = time.clock() - t0
        #print retVal
        print t1    #total test time
        print t3    #time to retrieve 1,000,000th answer
        self.assertTrue(addedOneMil)
    

    @requirements(['#0035'])
    def test_get_hdd_access_time(self):
        answer = self.obj.ask('What is the hard drive access time?')
        print answer
        self.assertLess(answer, 0.010)
        
    @requirements(['#0036'])
    def test_find_prime(self):
        answer = self.obj.ask('What is the 5 prime number?')
        print answer
        time.sleep(.01)
        answer = self.obj.ask('What is the 5 prime number?')
        self.assertEqual(answer, 11)
        
    @requirements(['#0037'])
    def test_find_pi(self):
        answer = self.obj.ask('What is the 10 number of pi?')
        print answer
        time.sleep(.01)
        answer = self.obj.ask('What is the 10 number of pi?')
        self.assertEqual(answer, 3)

    @requirements(['#0038'])
    def test_find_interest(self):
        answer = self.obj.ask('How much money will i have if i invest 1000 dollars at 2% for ten years?')
        print answer
        time.sleep(.1)
        answer = self.obj.ask('How much money will i have if i invest 1000 dollars at 2% for ten years?')
        self.assertEqual(answer, 1219.0)
