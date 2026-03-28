# Problem Statement

# Create a class Course for an online learning platform.

# Requirements:
    # Each course should have:
    # Course Name (public)
    # Instructor Name (public)
    # Course Price (private)
    # Course Code (protected)
    # Number of Students Enrolled (private)
# Platform should have:
    # Class variable platform_name = "CodeLearn"
    # Class variable total_courses to count how many courses are created.
# Methods:
    # enroll_student() → increases student count
    # get_price() → getter for private price
    # set_price(new_price) → setter for private price
    # apply_discount(percent)
    # display_course_info()
# Rules:
    # Price cannot be negative
    # Discount cannot reduce price below 0
    # Students count cannot be accessed directl

class Course:

    platform_name = 'TryHackMe'
    total_courses = 0

    def __init__(self, course_name, inst_name, code, price):
        self.course_name = course_name, 
        self.inst_name = inst_name, 
        self._code = code ,
        self.__price = price
        self.__student_enrolled = 0

        Course.total_courses += 1

    def enrolled_students(self):
        self.__student_enrolled += 1
        print("Enrollment Successful")

    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Invalid Amount")

    def apply_discount(self, percent):
        discount_amount = (self.__price * percent) / 100

        new_price = self.__price - discount_amount

        if new_price >= 0:
            self.__price = new_price
            print("Discounted")
        
        else:
            print("Sorry Discount can't be applied")
            
    def display_course_info(self):
        print("Platform: ", Course.platform_name)

        print("Course Name: ", self.course_name)

        print("Instructor: ", self.inst_name)

        print("Course Code", self._code)

        print("Price", self.__price)

        print("Enrollment", self.__student_enrolled)


c1 = Course("System Setup", "John", "SYS101", 3000)

C2 = Course("Pentseting Basics", "Marry", "PEN131", 7000)

c1.enrolled_students()
c1.enrolled_students()

c1.apply_discount(20)

c1.display_course_info()

print("Total Courses: ", Course.total_courses)


    