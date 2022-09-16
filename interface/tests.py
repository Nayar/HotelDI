from django.test import TestCase
from .models import *

class BookingTestCase(TestCase):
    def setUp(self):
        r1 = Room(room_trype="std",price=1000)
        r1.save()
        r2 = Room(room_trype="std",price=1000)
        r2.save()
        #pass

    def test_room_availability(self):
        rooms = Room.objects.all()
        self.assertEqual(len(rooms), 2)

        rooms = Room.search("2022-09-16","2022-09-17")
        self.assertEqual(len(rooms), 2)

        r1 = rooms[0]

        booking = r1.book("2022-09-16","2022-09-17","njoolfoo")
        self.assertEqual(booking.email, "njoolfoo")

        rooms = Room.search("2022-09-16","2022-09-19")
        self.assertEqual(len(rooms), 1)

        rooms = Room.search("2022-09-21","2022-09-22")
        self.assertEqual(len(rooms), 2)

        rooms[0].book("2022-09-21","2022-09-22","njoolfoo")
        rooms[1].book("2022-09-21","2022-09-25","njoolfoo")

        rooms = Room.search("2022-09-22","2022-09-23")
        self.assertEqual(len(rooms), 0)

        rooms = Room.search("2022-09-26","2022-09-28")
        self.assertEqual(len(rooms), 2)

        rooms[1].book("2022-09-27","2022-09-28","njoof")

        rooms = Room.search("2022-09-26","2022-09-28")
        self.assertEqual(len(rooms), 1)