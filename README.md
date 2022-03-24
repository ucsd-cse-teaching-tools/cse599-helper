This is a set of useful scripts and workflows for TAing CSE 599 Teaching Methods in Computer Science at the University of California, San Diego.

The following are some of the regular tasks that I am responsible for:

1) Mentor TA recruitment [Before quarter]
2) Assigning students to mentors [Week 1]
3) Deciding a time for and setting up the Practicum meetings for every group [Week 1]
4) Timely reminders about upcoming deadlines and synchronous meetings [ongoing]
5) Managing attendance for all synchronous components* [ongoing]
6) Grading make-up work for missed attendance [ongoing]
7) Managing Weekly Time Log + Reflection assignments 
    (a) Creating in Gradescope [Before quarter]
    (b) Spotting students of concern [ongoing]
    (c) Responding to student comments in victory / challenge questions [ongoing]
    (d) Collating student comments in open-ended questions and relaying to instructor each week [ongoing]
9) Tracking student progress and generating reports* [ongoing, esp. before Week 6 milestone]
10) Grading the Observation Reflection assignment [ongoing / end of quarter]
11) Grading the Teaching Resource Video [ongoing / end of quarter]
12) Grading the Scholarly Teaching Topic Quick Response assignments [ongoing /end of quarter]

*script in repo

I have outlined my experience and all the helpful advice that I have received from Professor Mia Minnes for each of my responsibilities.

#### 1. Mentor TA recruitment
- Mentors from a previous offering of CSE 599 can be contacted to see if they are interested in reprising their role.
- Post-quarter survey responses from students from the previous offering of CSE 599 include the level of interest they have to take up the responsibility of Mentor TA.
- It can also be helpful to keep track of those students that get back refusing the offer for the current quarter but show interest in a similar opportunity in the coming quarters.

#### 2. Assigning students to mentors
- Can generate groups of students in parallel with Mentor TA recruitment. 
-- Try to group people working on similar classes (e.g. introductory programming classes together, theoretical classes together, large project classes together). For class description: class number <= 100 indicates Lower Division. Among Lower Division classes, all except CSE 20 , CSE 21 are programming intensive. Undergraduate theory classes are CSE 20, CSE 21, CSE 101, CSE 105. Upper division undergraduate classes are the remaining course numbers between 100 and 199. For both Graduate and Undergraduate classes, the second digit reflect the sub-discipline of CSE: x0y is Theory, x1y is Software Engineering, x2y is Systems/Networking, x3y is PL/Compilers, x4y is Hardware/Architecture, x5y is AI/ML, x6y is Vision/Graphics, x7y is HCI/Robotics, x8y is Bioinformatics, x9y is Special Studies Courses.
-- Try to avoid having people who are TAing the *same* class in the same group
-- If possible, groups should have 0 or at least 2 members from minoritized identities
- Preferable to do so by matching the courses that the students are TAing, and the courses that the Mentors have experience TAing.
- Try to ensure an equal number of students per group
- Release a document on canvas with the names of the Mentor TAs with a list of the students assigned to their group. Send out an email to all students announcing the same.

#### 3. Deciding a time for and setting up the Practicum meetings for every group
- Use [When2meet](https://when2meet.com) and use Pacific Time to allow for consistency.
- (remote teaching) create recurring Zoom meetings on the decided time, making the Mentor TA for that group the co-host of that meeting.
  - set a weekly recurrence and end after N occurrences, where N is week number of the quarter when the last meeting is to be hosted
  - set 'Registration' to 'Required' and select 'Attendees register once and can attend any of the occurrences'. This ensures that the attendees are registered, and allows for       recording attendance based on Zoom-registered UCSD email.
  - make the Mentor TA of that group the co-host of the meeting
  - Save the meeting, then open it from My Meetings. Show all occurrences, then delete the occurrences when there is to be no Practicum meeting.

#### 4. Timely reminders about upcoming deadlines and synchronous meetings
- Use the 'Schedule Send' option to schedule an email to all the students who are to be included for the synchronous meeting or who are yet to meet the deadline for submitting their work.
  - Monday morning 8 am PST emails
  - Quick reminders 15 minutes before the decided time of the synchronous meeting
- Can prove helpful to do so before every synchronous discussion and practicum meeting, and the observation reflection deadline

#### 5. Managing attendance for all synchronous components*
- Create Gradescope templated assignments for each synchronous meeting for which attendance is to be tracked.
- Use the script **attendance/gen_pdf.py** with **GENERATE_TEMPLATE = True** to get the Outline to upload for the assignment.
- Align the boxes for PID and Name in front of the respective fields in the template.
- Save the assignment, then go to settings and change "Who will upload submissions?" to student to allow students to proactively submit make-up work

- When a session is over, get the list of the participants from Zoom -> Reports -> Usage -> <MeetingName> -> click on number of participants. Do not toggle 'Show unique users' since it has been known to ignore some unique users too.
- Download the list and threshold the duration according to the decided minimum attendance time.
- Paste the name, email and truth value to the Attendance sheet.
- Extract the email stem of each entry, in both the Attendance sheet as well as the newly pasted email column
- Do an INDIRECT(CONCAT("TRUTHVALCOL",MATCH("EMAILSTEMCELLINROSTER",EMAILSTEMRANGE,0))) to assign truth values against the roster from the newly pasted columns, with matching     based on email stem. Cut and paste values only, and then replace "N/A"s, checking for email stem mismatches just in case.
- Download this sheet, keep only the PID, LastName, FirstName, Email, Discussion, Practicum columns and name the sheet "WeekX.csv"
- Change the week number in **attendance/gen_pdf.py** and run the script to generate the separate PDFs for Discussion and Practicum, with one page per student.
- Go to the Attendance assignment for that week's discussion(practicum) on Gradescope, set the "Submission Type" to "Templated" to ensure auto matching against the outline.
- Now upload the discussion(practicum) PDF that was generated by gen_pdf.py
- Let Gradescope match it automatically, then browse through to confirm correctness and manually match any entries that haven't been matched.
- Move on to Grading, group all the Blank answers (corresponding to the PDF we just uploaded) and give them 1/1 grade.

#### 6. Grading make-up work for missed attendance
- Share with the students that reach out after missing a session, the make-up work. Inform them that they have to submit their work to the corresponding Attendance assignment on   Gradescope.
- If in case they have missed the late due date for it, ask them to share it with you and manually upload it for them.
- Review the work and record attendance

#### 7. Managing Weekly Time Log + Reflection assignments
- Need not do much except when students miss a due date, in which case ask them to share their responses by referring to questions from the corresponding assignment from a different week. We can then create a submission for them to the correct assignment on Gradescope

#### 8. Tracking student progress and generating reports*
- Create a CSV with student PID, last name, first name, email, and then a column each for every assignment and synchronous session for which attendance is to be tracked.
- You may find Gradescope CSE 599 -> Assignments -> Download Grades helpful in filling up the above CSV with truth values.
- Use the script in **progress report/gen_progrep.py** to generate a template and create an instructor-uploaded, templated submission assignment on Gradescope using the template   as an outline.
- Modify the script to include all components of the class that are in the CSV. Create conditions on them and the corresponding feedback to give to the students based on the       outcome of those conditions
- Run the script and upload the generated progress report PDF to the assignment on Gradescope that we just previously created.
- Follow the steps in **5** to publish the grades

#### 9. Grading Observation Reflection Assignment
- Review each submitted report on Gradescope, watch the uploaded videos for each, and leave encouraging and constructive feedback!
