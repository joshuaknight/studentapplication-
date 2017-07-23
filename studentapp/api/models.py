from django.db import models


class StudentModel(models.Model):
		roll_no  = models.CharField(max_length=30)
		name =  models.CharField(max_length=30)
		age  =  models.CharField(max_length=30)
		gender =  models.CharField(max_length=30,choices = [('Male',1),('Female',2)])

		def to_dict(self):
			return {
					'name' : self.name,
					'roll_no' : self.roll_no,
					'age' : self.age,
					'gender' : self.gender,
					}
