sList=[]
cList=[]
mList=[]
def input_students():
    totalstudents=int(input("Total Students: "))
    for i in range(0,totalstudents):
       sid=input("Enter your ID: ").strip()
       sname=input("Enter your name: ").strip()
       dob=input("Date of Birth: ").strip()
       sList.append({'ID':sid,'Name':sname,'DoB':dob})
def input_courses():
    totalcourses=int(input("Total courses: "))
    for i in range(0,totalcourses):
       cid=input("Enter the course ID: ").strip()
       cname=input("Name of the course: ").strip()
       cList.append({'Course ID':cid,'Course name':cname})
def input_mark():
    for courses in range(0,len(cList)):
        for students in range(0,len(sList)):
            mark=float(input(f"{sList[students].get('ID')},{cList[courses].get('Course ID')},Mark:"))
            mList.append({'Course':cList[courses],'Student':sList[students],'Mark':mark})
def list_course():
    for i in range(0,len(cList)):
        print(f"Course ID:{cList[i].get('Course ID')} Course name:{cList[i].get('Course name')}")
    print()
def list_students():
    for i in range(0,len(sList)):
        print(f"Student ID:{sList[i].get('ID')} Student name:{sList[i].get('Name')} DoB:{sList[i].get('DoB')}")
    print()
def list_mark():
    for i in range(0,len(mList)):
        print(f"Course ID:{mList[i].get('Course').get('Course ID')} Course name:{ mList[i].get('Course').get('Course name')}")       
        print(f"Student ID:{mList[i].get('Student').get('ID')} Student name:{mList[i].get('Student').get('Name')} DoB:{mList[i].get('Student').get('DoB')} Mark:{mList[i].get('Mark')}")
    print()
input_students()
input_courses()
input_mark()
list_course()
list_students()
list_mark()
    
    



    
    

