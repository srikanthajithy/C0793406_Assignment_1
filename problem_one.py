from lib.trains import Trains
from lib.routes import Routes
from lib.stops import Stop
from lib.Towns import Town
import unittest


class TrainsTests(unittest.TestCase):

    def setUp(self):
        print("setting up classes...")
        self.trains = Trains()
        self.routes = Routes()

        print("initializing towns...")
        self.a = Town('a')
        self.b = Town('b')
        self.c = Town('c')
        self.d = Town('d')
        self.e = Town('e')

        print("adding routes to route table...")
        self.routes.add_route_to_table(self.a, Stop(self.a, self.b, 5).next(
            Stop(self.a, self.d, 5).next(Stop(self.a, self.e, 7))))
        self.routes.add_route_to_table(self.b, Stop(self.b, self.c, 4))
        self.routes.add_route_to_table(self.c, Stop(self.c, self.d, 8).next(Stop(self.c, self.e, 2)))
        self.routes.add_route_to_table(self.d, Stop(self.d, self.c, 8).next(Stop(self.d, self.e, 6)))
        self.routes.add_route_to_table(self.e, Stop(self.e, self.b, 3))

    def test_read_input(self):
        print("verifying text file import...")
        self.assertNotEquals(self.trains.schedule_data, "")

    def test_train_array_exists(self):
        print("test existence of train routes...")
        routes = Routes()
        self.assertNotEquals(routes, [])

    def test_correct_data_type_from_route(self):
        print("asserting correct data types...")
        self.assertIsInstance(self.routes.route_table[self.a], Stop)
        self.assertIsInstance(self.routes.route_table[self.b], Stop)
        self.assertIsInstance(self.routes.route_table[self.c], Stop)
        self.assertIsInstance(self.routes.route_table[self.d], Stop)
        self.assertIsInstance(self.routes.route_table[self.e], Stop)

    def test_distance_of_route_ABC(self):
        scenario = '''
        1. The distance of the route A-B-C.
        Output #1: 9
        '''

        towns = [self.a, self.b, self.c]
        self.assertEquals(9, self.routes.distance_between_towns(towns))
        print("The distance of the route is ABC: ")

    def test_distance_of_route_AD(self):
        scenario = '''
        2. The distance of the route A-D.
        Output #2: 5
        '''
        print("The distance of the route is AD: ")
        towns = [self.a, self.d]
        self.assertEquals(5, self.routes.distance_between_towns(towns))

    def test_distance_of_route_ADC(self):
        scenario = '''
        3. The distance of the route A-D-C.
        Output #3: 13
        '''

        towns = [self.a, self.d, self.c]
        self.assertEquals(13, self.routes.distance_between_towns(towns))
        print("The distance of the route is ADC: ")

    def test_distance_of_route_AEBCD(self):
        scenario = '''
        4. The distance of the route A-E-B-C-D.
        Output #4: 22
        '''

        towns = [self.a, self.e, self.b, self.c, self.d]
        self.assertEquals(22, self.routes.distance_between_towns(towns))
        print("The distance of the route is AEBCD: ")

    def test_distance_of_route_AED(self):
        scenario = '''
        5. The distance of the route A-E-D.
        Output #5: NO SUCH ROUTE
        '''

        towns = [self.a, self.e, self.d]
        self.assertEquals("NO SUCH ROUTE", self.routes.distance_between_towns(towns))
        print("The distance of the route is AED:")

    def test_num_stops_C_to_C_3(self):
        scenario = '''
        6. The number of trips starting at C and ending at C with a maximum of 3
        stops.  In the sample data below, there are two such trips: C-D-C (2
        stops). and C-E-B-C (3 stops).
        Output #6: 2
        '''

        num_stops = self.routes.number_of_stops(self.c, self.c, 3)
        self.assertEquals(2, num_stops)
        print("The total no of stops is: ")

    def test_num_stops_A_to_C_4(self):
        scenario = '''
        7. The number of trips starting at A and ending at C with exactly 4 stops.
        In the sample data below, there are three such trips: A to C (via B,C,D); A
        to C (via D,C,D); and A to C (via D,E,B).
        Output #7: 3
        '''

        num_stops = self.routes.number_of_stops(self.a, self.c, 4)
        self.assertEquals(3, num_stops)
        print("The total no of stops is: ")

    def test_shortest_route_A_to_C(self):
        scenario = '''
        8. The length of the shortest route (in terms of distance to travel) from A
        to C.
        Output #8: 9
        '''

        shortest_route = self.routes.shortest_route(self.a, self.c)
        self.assertEquals(9, shortest_route)
        print("The shortest distance of the route is AC: ")

    def shortest_route_B_to_B(self):
        scenario = '''
        9. The length of the shortest route (in terms of distance to travel) from B
        to B.
        Output #9: 9
        '''

        shortest_route = self.routes.shortest_route(self.c, self.c)
        self.assertEquals(9, shortest_route)
        print("The shortest route is BB: ")

    def test_num_diff_routes_C_to_C_less_30(self):
        scenario = '''
        10. The number of different routes from C to C with a distance of less than 30.
        Output #10: 7
        '''

        num_routes_within = self.routes.num_routes_within(self.c, self.c, 30)
        self.assertEquals(7, num_routes_within)
        print("The number of different routes to CC: ")


def main():
    unittest.main()


