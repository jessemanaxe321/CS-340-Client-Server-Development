# CS-340 Client/Server Development

## Project Overview

This repository contains my CS 340 Project Two work for Grazioso Salvare. The project demonstrates how MongoDB, Python, and Dash can work together to create an interactive client/server application. The dashboard allows users to filter animal shelter data, view records in an interactive table, examine breed distributions, and view animal locations on a map.

## Reflection

### How do I write programs that are maintainable, readable, and adaptable?

I write maintainable and readable programs by separating responsibilities into smaller reusable components, using clear variable and function names, and commenting code where the purpose may not be immediately obvious. One of the strongest examples from this course was the CRUD Python module created in Project One. Instead of placing MongoDB operations directly inside the dashboard code, I created an `AnimalShelter` class that handled the Create, Read, Update, and Delete operations separately.

This made Project Two easier because the dashboard could reuse the same database module rather than repeating connection and query code. The dashboard only needed to call the CRUD methods and then focus on displaying and filtering the results. This approach also makes the code easier to maintain because changes to database access can be handled in one place. In the future, the same CRUD module could be reused for another dashboard, a command-line application, a reporting system, or another application that needs access to the same MongoDB database.

### How do I approach a problem as a computer scientist?

I approach a problem by first identifying the requirements and then separating the larger problem into smaller pieces that can be implemented and tested individually. For the Grazioso Salvare project, I first needed to understand what information the client needed from the Austin Animal Center dataset. I then created MongoDB queries for the different rescue types and connected those queries to interactive dashboard controls.

This project was different from many previous assignments because several technologies had to work together as one complete system. MongoDB handled the data, the Python CRUD module handled database communication, Pandas converted the data into a format that could be used by the dashboard, and Dash created the interface. I tested each part as I developed it instead of waiting until the entire project was complete. In future database projects, I would continue using this approach by defining requirements early, separating the data layer from the interface, developing reusable functions, and testing each component before integrating everything together.

### What do computer scientists do, and why does it matter?

Computer scientists use technology to solve problems, organize and analyze information, automate processes, and create systems that help people make better decisions. Their work matters because software can turn large amounts of raw data into useful information that would otherwise be difficult or time-consuming to analyze.

In this project, the dashboard helps Grazioso Salvare quickly identify dogs that match specific search-and-rescue requirements. Instead of manually reviewing thousands of animal records, users can select a rescue category and immediately see matching animals, breed information, and geographic locations. A system like this can reduce the time required to identify potential rescue animals and allow the organization to focus more of its effort on training and rescue operations.

## Project Artifacts

This repository includes:

- `ProjectTwoDashboard.ipynb` — interactive Grazioso Salvare dashboard
- `CRUD_Python_Module.py` — reusable MongoDB CRUD module
- `CS340_ProjectTwo_README_Jesse_Carles.docx` — Project Two documentation and testing evidence
- `Grazioso Salvare Logo.png` — dashboard branding asset

## Technologies Used

- Python
- MongoDB
- PyMongo
- Pandas
- Dash
- Plotly
- Dash Leaflet
- Jupyter Notebook
