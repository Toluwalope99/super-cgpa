#cgpa calculator
#last edit May 5, 2021

SemesterDict = {"F": "FIRST", "S": "SECOND"}

# semester lists
semester_list = []
session_list = []
part_list = []
count = 0
checker2 = True

# cumulative lists
cum_courseList = []
cum_courseGradeList = []
cum_courseScoreList = []
cum_courseUnitList = []
cum_courseTotalList = []


def identify():
    option = input("DO you want to enter your information firstly? Enter Y or N: ").upper()

    while option != "Y" and option != "N":
        option = input("WRONG! Please select Y or N: ").upper()

    if option == "Y":
        print("Input the details below before calculating, put NIL to skip any!")
        FirstName = input("Enter your first name here: ")
        LastName = input("Enter your surname here: ")
        MatNum = input("Enter your matriculation number here: ")
        Part = (input("Enter your part here, number only: "))
        Semester = input("Type F for first Semester and S for Second Semester: ").upper()
        Session = input("Enter Academic Session in the form: YYYY/YYYY: ")
    else:
        FirstName = ""
        LastName = ""
        MatNum = ""
        Part = "20"
        Semester = "F"
        Session = "4000/4001"

    print("\n" * 50)
    print("How do you want to enter your result?")
    gradeChoice = input("Please enter S to input your scores or G to enter the grade for each course: ").upper()

    while gradeChoice != "G" and gradeChoice != "S":
        gradeChoice = input("WRONG! Please select G (grade) or S (score): ").upper()

    return FirstName, LastName, MatNum, Part, Semester, Session, gradeChoice


def gradeOnly(grade_value):
    if grade_value == "A" or grade_value == "a":
        return 5
    elif grade_value == "B" or grade_value == "b":
        return 4
    elif grade_value == "C" or grade_value == "c":
        return 3
    elif grade_value == "D" or grade_value == "d":
        return 2
    elif grade_value == "E" or grade_value == "e":
        return 1
    elif grade_value == "F" or grade_value == "f":
        return 0


def gradeScore(score):
    if score in range(70, 101):
        return 5
    elif score in range(60, 70):
        return 4
    elif score in range(50, 60):
        return 3
    elif score in range(45, 50):
        return 2
    elif score in range(40, 45):
        return 1
    elif score in range(0, 40):
        return 0


def cgpaValue(gpa):
    if gpa >= 4.5:
        if gpa <= 5.0:
            return "FIRST CLASS!"

    if gpa < 4.5:
        if gpa >= 3.5:
            return "SECOND CLASS UPPER!"
    if gpa < 3.5:
        if gpa >= 2.5:
            return "SECOND CLASS LOWER!"
    if gpa < 2.5:
        if gpa >= 1.5:
            return "THIRD CLASS!"
    if gpa < 1.5:
        if gpa >= 1.0:
            return "PASS!"
    if gpa < 1.0:
        if gpa >= 0.0:
            return "FAIL!"
    else:
        print("INVALID GRADE VALUE")
        raise ValueError


def scoreValue(score):
    if score in range(70, 101):
        return "A"
    elif score in range(60, 70):
        return "B"
    elif score in range(50, 60):
        return "C"
    elif score in range(45, 50):
        return "D"
    elif score in range(40, 45):
        return "E"
    elif score in range(0, 40):
        return "F"


def gpa_calc(gradeChoice):
    counter = 0
    courseList = []

    print("\n" * 50)
    if len(semester_list) > 1:
        print("NEXT SEMESTER! \n")
    while counter == 0:
        course = input("Enter the name of your courses one after the other (enter = when all courses have been "
                       "inputted): ")
        if course == "=":
            break
        courseList.append(course.upper())
        cum_courseList.append(course.upper())

    n = len(courseList)

    print("The list of courses you registered this semester are: " + str(courseList))

    courseGradeList = []
    courseScoreList = []
    courseUnitList = []
    courseTotalList = []

    unit_error = False
    for course_name in courseList:
        try:
            courseUnit = int(input("Enter number of units for " + str(course_name) + " here: "))
            if courseUnit > 9:
                raise ValueError
        except ValueError:
            unit_error = True

        while unit_error:
            print("WRONG INPUT! Course unit must not exceed 9!")
            try:
                courseUnit = int(input("Enter the number of units for {} again: ".format(str(course_name))))
            except ValueError:
                continue
            if courseUnit in range(0, 10):
                unit_error = False
            else:
                unit_error = True

        courseUnitList.append(courseUnit)
        cum_courseUnitList.append(courseUnit)

    if gradeChoice == "G":
        grade_error = False
        for course_name in courseList:
            try:
                courseGrade = input("Enter your grade for " + str(course_name) + " here: ")
                if courseGrade not in ("A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"):
                    raise ValueError
            except ValueError:
                grade_error = True

            while grade_error:
                print("INVALID GRADE! Must be between A and F!")
                try:
                    courseGrade = input("Enter your grade for {} again: ".format(str(course_name)))
                except ValueError:
                    continue
                if courseGrade in ("A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"):
                    grade_error = False
                else:
                    grade_error = True

            courseGradeList.append(courseGrade.upper())
            cum_courseGradeList.append(courseGrade.upper())

    if gradeChoice == "S":
        score_error = False
        for course_name in courseList:
            try:
                courseScore = int(input("Enter your score for " + str(course_name) + " here: "))
                if courseScore not in range(0, 101):
                    raise ValueError
            except ValueError:
                score_error = True

            while score_error:
                print("Score is INVALID! Your score must be between 0 and 100!")
                try:
                    courseScore = int(input("Enter your score for " + str(course_name) + " again: "))
                except ValueError:
                    continue
                if courseScore in range(0, 101):
                    score_error = False
                else:
                    score_error = True

            courseScoreList.append(courseScore)
            cum_courseScoreList.append(courseScore)

    if gradeChoice == "G":
        count = 0
        while count < n:
            courseTotal = courseUnitList[count] * int(gradeOnly(courseGradeList[count]))
            courseTotalList.append(courseTotal)
            cum_courseTotalList.append(courseTotal)
            count += 1

    if gradeChoice == "S":
        count = 0
        while count < n:
            courseTotal = courseUnitList[count] * int(gradeScore(int(courseScoreList[count])))
            courseTotalList.append(courseTotal)
            cum_courseTotalList.append(courseTotal)
            count += 1

    cum_TotalPoint = 0
    TotalPoint = 0

    for Total in courseTotalList:
        TotalPoint += int(Total)

    for Total in cum_courseTotalList:
        cum_TotalPoint += int(Total)

    cum_TotalUnit = 0
    TotalUnit = 0

    for Unit in courseUnitList:
        TotalUnit += int(Unit)
    for Unit in cum_courseUnitList:
        cum_TotalUnit += int(Unit)

    prev_TotalPoint = cum_TotalPoint - TotalPoint
    prev_TotalUnit = cum_TotalUnit - TotalUnit

    GradePoint = TotalPoint / TotalUnit

    try:
        prev_GradePoint = prev_TotalPoint / prev_TotalUnit
    except ZeroDivisionError:
        prev_GradePoint = 0

    cum_GradePoint = cum_TotalPoint / cum_TotalUnit

    if gradeChoice == "G":
        return GradePoint, TotalPoint, TotalUnit, prev_GradePoint, prev_TotalPoint, prev_TotalUnit, cum_GradePoint, \
               cum_TotalPoint, cum_TotalUnit, courseList, courseUnitList, courseGradeList
    else:
        return GradePoint, TotalPoint, TotalUnit, prev_GradePoint, prev_TotalPoint, prev_TotalUnit, cum_GradePoint, \
               cum_TotalPoint, cum_TotalUnit, courseList, courseUnitList, courseScoreList


def result_display(gpa, tpts, tuts, pgpa, ptpts, ptuts, cgpa, ctpts, ctuts, fn, ln, mat, ses, sem, pt, grdCh, clst,
                   culst, chLst):
    # gpa = gpa, tpts = total points, tuts = total units
    # pgpa = previous gpa, ptpts = previous total points, ptuts = previous total units
    # cgpa = cumulative gpa, ctpts = cumulative total points, ctuts = cumulative total units
    # fn = first name, ln = last name, mat = matric number, ses = session, sem = semester, pt = part
    # grdCh = grade input choice, clst = course list, culst = course unit list
    # chLst = courseGradeList or courseScoreList
    print("\n" * 50)
    if int(ses[0:4]) < 4000:
        print("RESULT SUMMARY FOR THE " + str(SemesterDict[sem]) + " SEMESTER OF THE " + str(
        ses) + " ACADEMIC SESSION")
    if len(fn) > 1:
        print("Full name: " + fn + " " + ln)
    if len(mat) > 1:
        print("Matriculation Number: " + str(mat.upper()))
    if int(pt) < 20:
        print("Part: Part " + str(pt))
    print("==================================")
    print("COURSE LIST SUMMARY")
    print("==================================")

    n = len(clst)

    if grdCh == "G":
        for i in range(0, n):
            print(str(clst[i]) + ": \t" + str(culst[i]) + " units: \t" + str(chLst[i]))

    if grdCh == "S":
        for i in range(0, n):
            print(str(clst[i]) + ": \t" + str(culst[i]) + " units: \t" + str(chLst[i]) + str(scoreValue(chLst[i])))

    print()

    if len(semester_list) > 1:
        print("==================================")
        print("PREVIOUS")
        print("==================================")
        print("Total Number of Registered Units: " + str(ptuts))
        print("Total Number of Points: " + str(ptpts))
        print()
        print("PREVIOUS GPA: " + str(pgpa.__round__(2) + 0.00))
        print("PREVIOUS CLASS: {}".format(cgpaValue(pgpa)))
        print()

    if len(semester_list) > 0:
        print("==================================")
        print("PRESENT")
        print("==================================")
        print("Total Number of Registered Units: " + str(tuts))
        print("Total Number of Points: " + str(tpts))
        print()
        print("SEMESTER GPA: " + str(gpa.__round__(2) + 0.00))
        print("SEMESTER CLASS: {}".format(cgpaValue(gpa)))
        print()

    if len(semester_list) > 0:
        print("==================================")
        print("CUMULATIVE")
        print("==================================")
        print("Total Number of Registered Units: " + str(ctuts))
        print("Total Number of Points: " + str(ctpts))
        print()
        print("CUMULATIVE GPA: " + str(cgpa.__round__(2) + 0.00))
        print("CUMULATIVE CLASS: {}".format(cgpaValue(cgpa)))


def main():
    print("WELCOME TO THE SUPER CGPA CALCULATOR!!!")
    fn, ln, mat, pt, sem, ses, grdCh = identify()
    semester_list.append(sem)
    session_list.append(ses)
    part_list.append(pt)
    global checker2

    def add_semester(choice2):
        global count, checker2
        if choice2 == "Y":
            noted = semester_list[count]
            if noted == "F":
                sem = "S"
            else:
                sem = "F"
            semester_list.append(sem)

            okay = session_list[count]
            frspt = int(okay[0:4])
            secpt = int(okay[5:])
            if len(session_list) % 2 != 0:
                new1 = frspt
                new2 = secpt
            else:
                new1 = frspt + 1
                new2 = secpt + 1

            new_ses = str(new1) + "/" + str(new2)

            ses = new_ses
            session_list.append(ses)

            parted = part_list[count]
            if len(part_list) % 2 == 0:
                pt = str(int(parted) + 1)
            else:
                pt = parted

            part_list.append(str(pt))
            count += 1

            print("\n" * 50)
            gpa, tpts, tuts, pgpa, ptpts, ptuts, cgpa, ctpts, ctuts, clst, culst, chLst = gpa_calc(grdCh)

            result_display(gpa, tpts, tuts, pgpa, ptpts, ptuts, cgpa, ctpts, ctuts, fn, ln, mat, ses, sem, pt, grdCh,
                           clst, culst, chLst)
        else:
            checker2 = False

    gpa, tpts, tuts, pgpa, ptpts, ptuts, cgpa, ctpts, ctuts, clst, culst, chLst = gpa_calc(grdCh)

    result_display(gpa, tpts, tuts, pgpa, ptpts, ptuts, cgpa, ctpts, ctuts, fn, ln, mat, ses, sem, pt, grdCh, clst,
                   culst, chLst)

    while checker2:
        choice000 = input("Do you want to add another semester? Y or N: ").upper()

        while choice000 != "Y" and choice000 != "N":
            choice000 = input("WRONG! Please select Y or N to add another semester: ").upper()

        add_semester(choice000)

    while not checker2:
        print("\n" * 50)
        print("THANK YOU! APP WILL BE EXITED!")
        break

# call the main function
main()
