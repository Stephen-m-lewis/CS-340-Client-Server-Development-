# CS-340-Client-Server-Development-
Project Two README
Grazioso Salvare Dashboard
By: Stephen Lewis
Project Overview
The goal was to develop a web-based dashboard that allows Grazioso Salvare to interact with and visualize animal shelter data stored in MongoDB. The dashboard was created using Python, Dash, and MongoDB and provides an easy way to filter animal records based on rescue type requirements. The application displays an interactive data table, a geolocation map, and a chart that update dynamically when filters are selected.
The dashboard allows users to view all available animal records or filter them based on the rescue categories requested by Grazioso Salvare:
•	Water Rescue
•	Mountain/Wilderness Rescue
•	Disaster/Individual Tracking
•	Reset (unfiltered data)
The application was designed to provide a user-friendly interface that allows the client to quickly identify animals that meet specific rescue criteria.
 
Required Functionality
The completed dashboard includes all required functionality outlined in the project specifications.
Dashboard Features
•	Grazioso Salvare logo displayed on the dashboard
•	Unique identifier displaying my name
•	Interactive radio button filters
•	Interactive data table connected to MongoDB
•	Geolocation map showing animal locations
•	Pie chart displaying breed distributions
•	Dynamic updates when rescue filters are selected
Starting Dashboard State
The dashboard initially loads all records from the MongoDB database and displays them in the interactive data table.
Screenshot 1 – Starting Dashboard State
(Insert Screenshot 1 here) 
 
Water Rescue Filter
The Water Rescue filter displays animals that match the requirements for water rescue operations. The data table, pie chart, and map update automatically when this filter is selected.
Screenshot 2 – Water Rescue Filter
(Insert Screenshot 2 here) 
 
Mountain/Wilderness Rescue Filter
The Mountain/Wilderness Rescue filter displays animals that match the criteria for mountain and wilderness rescue operations.
Screenshot 3 – Mountain/Wilderness Rescue Filter
(Insert Screenshot 3 here) 
Disaster/Individual Tracking Filter
The Disaster/Individual Tracking filter displays animals that match the disaster rescue and tracking requirements provided by Grazioso Salvare.
Screenshot 4 – Disaster/Individual Tracking Filter
(Insert Screenshot 4 here) 
Reset Filter
The Reset filter restores the dashboard to its original unfiltered state and displays all available records.
Screenshot 5 – Reset Filter
(Insert Screenshot 5 here) 
 
Tools and Technologies Used
MongoDB
MongoDB was used as the database component of the application. MongoDB is a document-based NoSQL database that stores data in JSON-like documents. This structure makes it easy to work with Python because MongoDB documents can be accessed as dictionaries and converted directly into Pandas DataFrames.
MongoDB was selected because it provides:
•	Flexible document storage
•	Fast querying capabilities
•	Easy integration with Python through PyMongo
•	Scalability for larger datasets
PyMongo
PyMongo was used to connect Python to MongoDB. The CRUD Python module created in Project One used PyMongo to retrieve records from the database and provide filtered query results to the dashboard.
Dash Framework
Dash was used to create the web application interface. Dash provides both the view and controller components of the application. It allows interactive elements, such as radio buttons and tables, to communicate through callback functions.
Dash was used to create:
•	Interactive filters
•	Data tables
•	Pie chart visualization
•	Dashboard layout
Dash Leaflet
Dash Leaflet was used to create the geolocation map. The library allows animal locations to be displayed visually on an interactive map using latitude and longitude coordinates stored in the database.
Pandas
Pandas was used to convert MongoDB query results into DataFrames that could be displayed and manipulated within the dashboard.
Plotly Express
Plotly Express was used to create the pie chart showing the distribution of animal breeds returned by each rescue filter.
Resources Used
•	MongoDB Documentation
•	PyMongo Documentation
•	Dash Documentation
•	Dash Leaflet Documentation
•	SNHU CS-340 Module Resources
•	Dashboard Specifications Document
 
Steps Taken to Complete the Project
1.	Created and tested the CRUD Python module during Project One.
2.	Connected the dashboard application to MongoDB using the CRUD module.
3.	Retrieved all records from the database and displayed them in an interactive data table.
4.	Added the Grazioso Salvare logo and my name to the dashboard.
5.	Created radio button controls to allow users to select rescue categories.
6.	Developed MongoDB queries for Water Rescue, Mountain/Wilderness Rescue, and Disaster/Individual Tracking.
7.	Connected the filters to the dashboard using Dash callback functions.
8.	Added a pie chart that updates based on the selected rescue filter.
9.	Added a geolocation map that updates based on the selected record in the data table.
10.	Tested all dashboard functionality and verified that the table, chart, and map updated correctly.
 
Challenges Encountered
A challenge I encountered was connecting the interactive dashboard components together using Dash callback functions. Since the data table, chart, and map all depend on the selected filter, each component needed to update dynamically when a user interacted with the dashboard.
Another challenge involved working with MongoDB data inside Dash. MongoDB returns an ObjectId field that caused issues when loading the data into the dashboard table. The problem was solved by removing the _id field before loading the data into the Pandas DataFrame.
I also encountered an issue with the map and table callbacks during testing. Some callbacks were receiving empty values when the dashboard first loaded, which caused errors. I resolved this by adding checks to handle empty or missing selections before processing the data.
 
Reflection Questions
How do you write programs that are maintainable, readable, and adaptable? What were the advantages of working this way? How else could you use the CRUD Python module in the future?
One thing I learned from this project is breaking code into separate pieces makes it much easier to work with. Creating the CRUD Python module allowed me to keep all the database operations in one place instead of mixing them into the dashboard code. It made the dashboard easier to read and made it simpler to fix problems or add new features later. If I ever needed to change how the database connection or queries worked, I would only have to update the CRUD module instead of searching through the entire project. I could also reuse the same CRUD module in future projects that use MongoDB because the basic create, read, update, and delete functions would already be built.
How do you approach a problem as a computer scientist? How did your approach to this project differ from previous assignments? What techniques or strategies would you use in the future?
For the project, I focused on solving one problem at a time instead of trying to finish everything at once. I started by making sure the database connection worked, then tested each CRUD function before connecting it to the dashboard. After that, I added the filters, map, and chart one feature at a time and tested each one before moving on. This project was different from some of my earlier assignments because I had to combine several technologies, including Python, MongoDB, Dash, and Plotly, into one application. In the future, I would continue using this step-by-step approach because it makes it easier to find problems and keeps the project more organized.
What do computer scientists do, and why does it matter? How would your work on this type of project help a company like Grazioso Salvare do its work better?
Computer scientists create software that helps people solve problems and work more efficiently. In this project, the dashboard makes it much easier for Grazioso Salvare to search through animal shelter records, apply filters, and view information on a map instead of looking through thousands of records manually. This helps the organization find animals that meet specific rescue requirements faster and gives them the information they need to make better decisions. Projects like this show how software can turn large amounts of data into something that is useful and easy to understand.
<img width="468" height="641" alt="image" src="https://github.com/user-attachments/assets/e83a6307-8a59-445d-9879-7481f44bfcd2" />
