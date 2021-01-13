This is a set of useful scripts and workflows for TAing CSE 599 Teaching Methods in Computer Science at the University of California, San Diego.

The following are some of the regular tasks that I am responsible for:

1) Mentor TA recruitment
2) Assigning students to mentors
3) Deciding a time for and setting up the Practicum meetings for every group
4) Timely reminders about upcoming deadlines and synchronous meetings
5) Managing attendance for all synchronous components*
6) Grading make-up work for missed attendance
7) Managing time log + reflection submissions
8) Tracking student progress and generating reports*
9) Grading the Observation Reflection assignment

*script in repo

I have outlined my experience and all the helpful advice that I have received from Professor Mia Minnes for each of my responsibilities.

#### 1. Mentor TA recruitment
- Mentors from a previous offering of CSE 599 can be contacted to see if they are interested in reprising their role.
- Post-quarter survey responses from students from the previous offering of CSE 599 include the level of interest they have to take up the responsibility of Mentor TA.
- It can also be helpful to keep track of those students that get back refusing the offer for the current quarter but show interest in a similar opportunity in the coming quarters.

#### 2. Assigning students to mentors
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

- When a session is over, get the list of the participants from Zoom -> Reports -> Usage -> <MeetingName> -> click on number of participants. Do not toggle 'Show unique users' since it has been known to ignore some unique users too.
- Download the list and threshold the duration according to the decided time 
