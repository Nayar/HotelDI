from django.db import models

class Booking(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    number_of_person_per_room=models.IntegerField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    booking_date = models.DateField()
    additional_info = models.TextField()
    room = models.ForeignKey('Room',on_delete=models.CASCADE, null=True,default=None,blank=True)

    def __str__(self) :
        return f'{self.first_name} {self.last_name}'

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length=100)
    date_join = models.DateField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Review(models.Model):
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        return f'{self.email}'

class Room(models.Model):
    rt = [("std","Standard"),("de","Delux"),("sin","Single"),("db","Double")]
    room_trype = models.CharField(max_length=3, choices = rt)
    price = models.IntegerField()
    
    @classmethod
    def search(cls,date_in,date_out):
        available_rooms = []
        rooms = Room.objects.all()
        for room in rooms:
            bookings = Booking.objects.filter(
                    models.Q(room=room) & (
                    models.Q(checkin_date__lte=date_in) & models.Q(checkout_date__gte=date_in) |
                    models.Q(checkin_date__lte=date_out) & models.Q(checkout_date__gte=date_out)
                ))
            if(len(bookings) == 0):
                available_rooms.append(room)
        return available_rooms

    def book(self,date_in,date_out,email):
        b = Booking(first_name = "a",
            last_name = "a",
            phone_number = "a",
            email = email,
            number_of_person_per_room=2,
            checkin_date = date_in,
            checkout_date = date_out,
            booking_date = date_in,
            additional_info = 'a',
            room = self)
        b.save()
        return b

class Vacancies(models.Model):
    September=models.DateField()
    October=models.DateField()
    November=models.DateField()

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    questions=models.TextField()





        


