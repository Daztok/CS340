CS 340 README Joel Hays

**Q: How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?**

A: Writing maintainable, readable, and adaptable code involves following best practices like modularity, clearly naming variables, and thorough documentation. The CRUD Python module, developed for the dashboard is fairly straightforward in order to connect the database and extend functionality in future projects. This approach ensures current success and prepares the groundwork for future enhancements and scalability.

**Q: How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?**

A: Approaching problems as a computer scientist means breaking down complex requirements into manageable tasks and systematically addressing them. For the Grazioso Salvare project, I identified key requirements laid out in the assignments, performed goals in steps, and systematically integrated them. Unlike previous coursework, this project emphasized real-world application and client needs, showing the importance of adaptability and user-centric design. Moving forward, I’ll continue using structured problem-solving techniques to effectively meet client requirements.

**Q: What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?**

A: Computer scientists play a crucial role in designing and implementing solutions that solve real-world problems and improve efficiency. My work on the Grazioso Salvare project supports the company by streamlining the process of identifying and categorizing rescue dogs, which enhanced operational efficiency. This project shows how effective software development can significantly impact organizational success, and demonstrates the value of computer science in practical ways.

Project Overview
The Grazioso Salvare Dashboard is a user-friendly web application designed to help the Grazioso Salvare organization identify and categorize dogs suitable for search-and-rescue training within the Austin, Texas region. The dashboard interfaces with a MongoDB database to dynamically display and filter data, providing valuable insights through various interactive widgets and charts.
Required Functionality
The dashboard includes the following functionalities:
1.	Interactive Filters: Options to filter data based on rescue types:
o	Water Rescue
o	Mountain or Wilderness Rescue
o	Disaster or Individual Tracking
o	Reset (to view all data)
2.	Dynamic Data Table: Displays relevant information such as animal ID, breed, color, age, and location, and updates based on selected filters.
3.	Geolocation Chart: Shows the exact location of the selected dog within the Austin, Texas region.
4.	Bar Chart: Displays the ages of dogs by breed, updating dynamically based on selected filters.
5.	Branding: Includes the Grazioso Salvare logo** and a unique identifier with the developer's name.
Non-verbal Video Demonstration Link:
https://www.loom.com/share/9f739d0130484ae08e4704fd96b9bbd0?sid=9b42e3c3-661c-4ad2-8650-12afb2f03623
Tools used:
•	MongoDB: Used due to its ease of scale, flexibility and seamless integration for use with datasets.
•	Dash Framework: 
o	Allows for highly interactive web applications with minimal code
o	Integration with plotly allows the use of different visualization tools like graphs and charts
o	Ease of use allows more focus on content rather than how to make it work
•	PyMongo: Allows integration between python coding language and MongoDB(NoSQL)
•	Jupyter Notebook: An open-source web application that allows you to create and share documents that contain live code. Used for the interactive environment, visualization support, and easy documentation.
Project Implementation Steps
1.	Set Up MongoDB:
o	Installed and configured MongoDB locally.
o	Created a database and collection to store the animal shelter data.
o	Loaded the Austin Animal Center Outcomes dataset into the MongoDB collection.
2.	Develop CRUD Module(Project 1):
o	Implemented a Python module for CRUD operations using PyMongo.
o	Ensured the module could perform create, read, update, and delete operations on the MongoDB collection.
3.	Design Dashboard Layout:
o	Set up the initial layout of the dashboard using Dash.
o	Created components for the data table, geolocation chart, and bar chart.
o	Included the Grazioso Salvare logo** and unique identifier.
4.	Implement Interactive Filters:
o	Added dropdowns for filtering data based on rescue types.
o	Developed callback functions to update the data table, geolocation chart, and bar chart based on selected filters.
5.	Test and Deploy Dashboard:
o	Ran the dashboard locally to ensure all components and filters functioned correctly.
o	Captured screencast of the dashboard for database demonstration.

Challenges and Conclusion:
This Project was interesting with the integration of Python and NoSQL. This was also the first time I have been exposed to a Linux based OS. Newer challenges were incorporating the logo into the finished product. I was having trouble finding its location and mapping it in the Jupyter portal. Furthermore, I was having trouble with sorting because there are many mixed breeds in the database. This caused me to find a way to allow for anything containing any of the breeds required using the $regex query. 

Note** The logo icon is accessed via a created assets file in Jupyter Notebook
