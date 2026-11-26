def student_marks(**kwargs): 
   for subject, mark in kwargs.items():        print(subject, ":", mark) 

student_marks(name="sujith", Python=90, Maths=85, English=80)