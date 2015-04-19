import unittest
from copy import copy
from table import Table
<<<<<<< HEAD
def merge_dicts(a, b):
    c = a.copy()
    c.update(b)
    return c
import sqlite3
conn = sqlite3.connect('state.db')
c = conn.cursor()


# class TestTableIsOn(unittest.TestCase):

#     def setUp(self):
#         self.table = Table("initial_table")
        
#     def test_null(self):
#         # if point is null then the table is off
#         self.table.set_point()
#         value = self.table.is_on
#         self.assertEqual(value, False)
        
#     def test_on(self):
#         # if point is not null, the table is on
#         self.table.set_point(4)
#         value = self.table.is_on
#         self.assertEqual(value, True)

# class TestSetPoint(unittest.TestCase):
    
#     def setUp(self):
#         self.table = Table("initial_table")

#     def test_set_point_four(self):
#         #point is valid if value is 4
#         self.table.eval_roll(4)
#         value = self.table.point
#         self.assertEqual(value, 4)

#     def test_set_point_five(self):
#         #point is valid if value is 5
#         self.table.eval_roll(5)
#         value = self.table.point
#         self.assertEqual(value, 5)

#     def test_set_point_six(self):
#         #point is valid if value is 6
#         self.table.eval_roll(6)
#         value = self.table.point
#         self.assertEqual(value, 6)

#     def test_set_point_eight(self):
#         #point is valid if value is 8
#         self.table.eval_roll(8)
#         value = self.table.point
#         self.assertEqual(value, 8)

#     def test_set_point_nine(self):
#         #point is valid if value is 9
#         self.table.eval_roll(9)
#         value = self.table.point
#         self.assertEqual(value, 9)

#     def test_set_point_ten(self):
#         #point is valid if value is 10
#         self.table.eval_roll(10)
#         value = self.table.point
#         self.assertEqual(value, 10)

#     def test_set_point_two(self):
#         #point is not valid if value is 2
#         self.table.eval_roll(11)
#         value = self.table.point
#         self.assertEqual(value, None)

#     def test_set_point_three(self):
#         #point is not valid if value is 3
#         self.table.eval_roll(3)
#         value = self.table.point
#         self.assertEqual(value, None)

#     def test_set_point_seven(self):
#         #point is not valid if value is 7
#         self.table.eval_roll(7)
#         value = self.table.point
#         self.assertEqual(value, None)

#     def test_set_point_eleven(self):
#         #point is not valid if value is 11
#         self.table.eval_roll(11)
#         value = self.table.point
#         self.assertEqual(value, None)

#     def test_set_point_twelve(self):
#         #point is not valid if value is 12
#         self.table.eval_roll(12)
#         value = self.table.point
#         self.assertEqual(value, None)

# class TestRoll(unittest.TestCase):
    
#     def setUp(self):
#         self.table = Table("initial_table")

#     def test_roll_random(self):
#         #test a randomly generated dice roll
#         value1 = [self.table.roll_dice() for i in range(10)]
#         value2 = [self.table.roll_dice() for i in range(10)]
#         self.assertNotEqual(value1, value2)

# class TestRollPoint(unittest.TestCase):
    
#     def setUp(self):
#         self.table = Table("initial_table")

#     def test_roll_valid_point_table_off(self):
#         #test roll valid point with table off
#         self.assertFalse(self.table.is_on)
#         self.table.roll_dice = lambda: 4
#         self.table.shoot()
#         value = self.table.point
#         self.assertEqual(value, 4)
#         self.assertTrue(self.table.is_on)


#     def test_roll_invalid_point_table_off(self):
#         #test roll invalid point with table off
#         self.assertFalse(self.table.is_on)
#         self.table.roll_dice = lambda: 12
#         self.table.shoot()
#         value = self.table.point
#         self.assertEqual(value, None)
#         self.assertFalse(self.table.is_on)
        
#     def test_roll_valid_point_table_on(self):
#         #test roll with non-pass point  and non-craps with table on and point set
#         self.table.eval_roll(9)
#         self.assertTrue(self.table.is_on)
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         value = self.table.point
#         self.assertEqual(value, 9)
#         self.assertTrue(self.table.is_on)

#     def test_roll_craps_table_on(self):
#         #test roll craps with table on and point set
#         self.table.set_point(9)
#         self.assertTrue(self.table.is_on)
#         self.table.roll_dice = lambda: 7
#         self.table.shoot()
#         value = self.table.point
#         self.assertEqual(value, None)
#         self.assertFalse(self.table.is_on)


#     def test_roll_pass_point_table_on(self):
#         #test roll pass with table on and point set
#         self.table.set_point(9)
#         self.assertTrue(self.table.is_on)
#         self.table.roll_dice = lambda: 9
#         self.table.shoot()
#         value = self.table.point
#         self.assertEqual(value, None)
#         self.assertFalse(self.table.is_on)


# class TestPlaceBet(unittest.TestCase):
    
#     def setUp(self):
#         self.table = Table("initial_table")

#     def test_place_pass_bet(self):
#         self.table.place_bet({'pass_line': 10})
#         value = self.table.list_all_bets()
#         self.assertEqual(value, {'pass_line': 10})
        
#     def test_payout_pass_bet_10(self):
#         self.table.place_bet({'pass_line': 10})
#         self.assertEqual(self.table.bank, 90)
#         self.table.set_point(9)
#         self.table.roll_dice = lambda: 9
#         self.table.shoot()
#         self.assertEqual(self.table.bank, 100)

#     def  test_payout_pass_bet_20(self):
#         self.table.place_bet({'pass_line': 20})
#         self.assertEqual(self.table.bank, 80)
#         self.table.set_point(9)
#         self.assertTrue(self.table.is_on)
#         self.table.roll_dice = lambda: 9
#         self.table.shoot()
#         self.assertEqual(self.table.bank, 100)
        
# class TestStatus(unittest.TestCase):
    
#     def setUp(self):
#         self.table = Table("initial_table")
#         self.default_status = {
#             "is_on": False,
#             "point": None,
#             "placed_bets": {"pass_line": 10},
#             "open_bets": [],
#             "bank": 90
#             }
            
#     def test_initial_status_report(self):
#         #Game Start - Table Off, No Point, No Bets, Initial Bank, Pass Line Available
#         value = {}
#         value = self.table.status()
#         self.assertEqual(value, merge_dicts(self.default_status, {
#                 "placed_bets": {},
#                 "open_bets": ["pass_line"],
#                 "bank": 100                
#                 }))

        
#     def test_initial_status_report_first_bet(self):
#         #First Bet - Table Off, No Point, Pass Bet - 10, Bank - 90, No Bets Available
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         value = self.table.status()
#         self.assertEqual(value, self.default_status)
        
#     def test_initial_status_report_first_roll_craps(self):
#         #Roll Craps - Table Off, No Point, Pass Bet - 0, Bank - 90, Pass Bet Available
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         self.table.roll_dice = lambda: 2
#         self.table.shoot()
#         value = self.table.status()
#         self.default_status.update({
#                 "placed_bets": {},
#                 "open_bets": ["pass_line"]
#                 })
#         self.assertEqual(value, self.default_status)
        
#     def test_initial_status_report_first_roll_pass(self):
#         #Roll Pass - Table Off, No Point, Pass Bet - 10, Bank - 100
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         self.table.roll_dice = lambda: 7
#         self.table.shoot()
#         value = self.table.status()
#         self.default_status.update({
#                 "bank": 100                
#                 })
#         self.assertEqual(value, self.default_status)

#     def test_initial_status_report_first_roll_point(self):
#         #Roll Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         value = self.table.status()
#         self.default_status.update({
#                 "is_on": True,
#                 "point": 6,
#                 "open_bets": ["non_point"],
#                 })
#         self.assertEqual(value, self.default_status)

#     def test_initial_status_report_bet_non_point(self):
#         #Bet Non_Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         self.table.place_bet({'non_point': 20})
#         value = self.table.status()
#         self.default_status.update({
#                 "is_on": True,
#                 "point": 6,
#                 "placed_bets": {"pass_line": 10, "non_point": 20},
#                 "bank": 70
#                 })
#         self.assertEqual(value, self.default_status)

#     def test_initial_status_report_second_roll_craps(self):
#         #Bet Non_Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         self.table.place_bet({'non_point': 20})
#         self.table.roll_dice = lambda: 7
#         self.table.shoot()
#         value = self.table.status()
#         self.default_status.update({
#                 "placed_bets": {},
#                 "open_bets": ["pass_line"],
#                 "bank": 70
#                 })
#         self.assertEqual(value, self.default_status)

#     def test_initial_status_report_second_roll_point(self):
#         #Bet Non_Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         self.table.place_bet({'non_point': 20})
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         value = self.table.status()
#         self.default_status.update({
#                 "placed_bets": {"pass_line": 10, "non_point": 20},
#                 "bank": 80
#                 })
#         self.assertEqual(value, self.default_status)

#     def test_initial_status_report_second_roll_point_no_pass_bet(self):
#         #Bet Non_Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
#         value = {}
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         self.table.place_bet({'non_point': 20})
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         value = self.table.status()
#         self.default_status.update({
#                 "placed_bets": {"non_point": 20},
#                 "open_bets": ["pass_line"],
#                 "bank": 80
#                 })
#         self.assertEqual(value, self.default_status)


#     def test_initial_status_report_second_roll_non_point(self):
#         #Bet Non_Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         self.table.place_bet({'non_point': 20})
#         self.table.roll_dice = lambda: 9
#         self.table.shoot()
#         value = self.table.status()
#         self.default_status.update({
#                 "is_on": True,
#                 "point": 6,
#                 "placed_bets": {"pass_line": 10, "non_point": 20},
#                 "bank": 85
#                 })
#         self.assertEqual(value, self.default_status)

#     def test_initial_status_report_second_roll_non_point_no_non_point_bet(self):
#         #Bet Non_Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
#         value = {}
#         self.table.place_bet({'pass_line': 10})
#         self.table.roll_dice = lambda: 6
#         self.table.shoot()
#         self.table.roll_dice = lambda: 9
#         self.table.shoot()
#         value = self.table.status()
#         self.default_status.update({
#                 "is_on": True,
#                 "point": 6,
#                 "open_bets": ["non_point"],
#                 "bank": 90
#                 })
#         self.assertEqual(value, self.default_status)

# class TestValidateBet(unittest.TestCase):

#     def setUp(self):
#         self.table = Table("initial_table")

#     def test_validate_true(self):
#         bet_amount = 10
#         self.assertTrue(self.table.validate_bet(bet_amount))

#     def test_validate_false(self):
#         bet_amount = 120
#         value = self.table.validate_bet(bet_amount)
#         print(value)
#         self.assertEqual(value, False)

#     def test_validate_true_bank(self):
#         self.table.bank = 200
#         status = self.table.status()
#         bet_amount = status['bank'] - 1
#         value = self.table.validate_bet(bet_amount)
#         self.assertTrue(value)
        
#     def test_validate_false_bank(self):
#         self.table.bank = 200
#         status = self.table.status()
#         bet_amount = status['bank'] + 1
#         value = self.table.validate_bet(bet_amount)
#         self.assertFalse(value)


class TestSaveState(unittest.TestCase):

    def test_load_bank(self):
        self.table = Table('initial_table')
        self.table.load_bank('initial_table')
        status = self.table.status()
        self.assertEqual(status['bank'], 100)

    def test_load_is_on(self):
        self.table = Table('initial_table')
        status = self.table.status()
        self.assertFalse(status['is_on'])
        
    def test_save_state(self):
        self.table = Table('saved_table')
        self.table.change_bank(50, 'minus')
        status = self.table.status()
        self.assertEqual(status['bank'], 50)
        self.table = Table('saved_table')
        self.table.change_bank(10, 'minus')
        status = self.table.status()
        self.assertEqual(status['bank'], 40)

    def tearDown(self):
        c.execute("DELETE FROM status where id = ?", ('saved_table',))
        conn.commit()
=======
from table import ArgumentException

class TableTest(unittest.TestCase):
    INITIAL_STATUS = {
            'bank': 100,
            'is_on': False,
            'available_bets': ['pass'],
            'placed_bets': {}
        }
    
    def test_initial_status(self):
        table = Table()
        expected_result = self.INITIAL_STATUS
        
        result = table.status()
        self.assertEqual(expected_result, result)


    def test_altered_status(self):
        status = {
            'bank': 50,
            'is_on': True,
            'available_bets': ['4', '5', '6', '8', '9', '10'],
            'placed_bets': {'6': 1}
        }
        
        table = Table(status)
        expected_result = status
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
 
    def test_set_status_on(self):
        table = Table()
        
        expected_result = copy(self.INITIAL_STATUS)
        expected_result['is_on'] = True
        table.set_on()
        
        result = table.status()
        self.assertEqual(expected_result, result)
 

 
    def test_set_status_off(self):
        initial_status = copy(self.INITIAL_STATUS)
        initial_status['is_on'] = True
        table = Table(initial_status)
 
        expected_result = self.INITIAL_STATUS
        table.set_off()
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
    def test_increment_bank(self):
        table = Table()
        
        expected_result = copy(self.INITIAL_STATUS)
        expected_result['bank'] = 101
 
        table.increment_bank(1)
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
    def test_decrement_bank(self):
        table = Table()
        
        expected_result = copy(self.INITIAL_STATUS)
        expected_result['bank'] = 99
 
        table.decrement_bank(1)
        
        result = table.status()
        self.assertEqual(expected_result, result)


    def test_place_bet(self):
        table = Table()
        
        expected_result = copy(self.INITIAL_STATUS)
        expected_result['placed_bets'] = {'pass': 1}
 
        table.place_bet('pass', 1)
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
        table.place_bet('pass', 1)
        expected_result['placed_bets'] = {'pass': 2}
        
        for bet in ['-3', '1', '0', '13']:
            with self.assertRaisesRegex(ArgumentException, "That is not a valid bet"):
                table.place_bet(bet, 1)
                
        for bet in ['4', '5', '6', '8', '9', '10']:
            with self.assertRaisesRegex(ArgumentException, "That is not a valid bet when the table is off"):
                table.place_bet(bet, 1)
                
 
 
>>>>>>> origin/master

        
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
    
    
