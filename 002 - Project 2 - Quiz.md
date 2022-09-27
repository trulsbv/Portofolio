<h3>Project 2, Quiz - Fall 2021</h3>
Link: https://github.com/trulsbv/Portofolio/blob/main/project_2_Quiz.zip

Run "hovedprogram" to start the program



![image](https://media.github.uio.no/user/8067/files/d9410081-6bec-4b5c-afe1-bff119ae9aac)

This is the home page of my quiz. Here you can choose between the different categories - at the moment the only category with real questions and answers is "Den unge biologen" - this is due to the fact that each questiion had to be manually added at the time of making this program. At the bottom the user can choose what amount of questions they want to get. If the category does not have eg. 50 questions - all avaliable questions will be presented.

In order to avoid a user just memorizing the pattern of questions or answers - both are displayed at random. This means that question [1, 2, 3, 4] might be presented to the user as [3, 1, 4, 2]. The same goes for the answers.

![image](https://media.github.uio.no/user/8067/files/744f6b63-716a-458c-a6e9-69fb98afdfcc)

A random question with its answers 

![image](https://media.github.uio.no/user/8067/files/b5196679-fb98-4c41-a84d-01218d957e79)

Here we see that questions can be added with photos

![image](https://media.github.uio.no/user/8067/files/c05ccba7-ca99-43a7-9f4e-0453d924d1cd)

At the end of the quiz you are given a score and the correct answer to the questions - as well as your answer.

The quiz is coded in JavaScript, CSS and HTML

While creating this quiz I encountered multiple obsticles - the first one was how to save the questions. I was at the first semester at the University of Oslo - and I had yet to begin at a "non-introductionary" course. I decided that the way I was going to save all the information was with an array. So all the questions are buildt up with a large array, where each element is another array like so: ["", ["", "", "", ""], " ", 0]. 
Index 0 is the quesion itself. 
Index 1 is a list with the four alternative answers. 
Index 2 is the correct answer.
And index 3, if not a 0, is the link (or in my case - the path) to the picture associated with the question


If I am going to improve on this quiz I would save the pictures externally and just get the pictures when needed. I would also create different styles of text-picture layout, this way it would be possible for a question to have none to multiple pictures, and they can be placed at different places in the text. Some questions need a picture at the begining, some in the middle and others at the end. I would also attempt use a database for the questions. I would also create a program where I could copy-paste the questions from the exam .pdf files and format them correctly
