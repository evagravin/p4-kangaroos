# The Smack
# _by the p4-kangaroos_
TheSmack is an aspiring social media site where users can share messages and emotions with friends, using inspiration from Twitter and TheSLAP.


## [Project Plan](https://docs.google.com/document/d/1iicxZwL0Sfc2mNzfxLqNAFXM357XP-C96Gz30Cukj44/edit)

## [TheSmack Website URL](http://goodtunes.cf/)

## [Scrum Board](https://github.com/evagravin/p4-kangaroos/projects/1)

Download our project via Intellij to view our blueprint layout and run our website, or view the Github files!


## Table of Collaborators:
| Name | Github Account |
| ------------- | ----------- | 
|Eva Gravin | [Github](https://github.com/evagravin) |
|Ava Brooks | [Github](https://github.com/avabrooks) |
|Risa Iwazaki | [Github](https://github.com/risaiwazaki) |
|Linda Long | [Github](https://github.com/lindalonglong) |

## Individual Mini-Labs
### Ava: 
 - [Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57952437)
 - Project concept: Display mean, median, mode of any data set that a user enters
 - Binary Grading:
     1. Use an individual section (blueprint) in your Scrum Team project for Mini Lab definition and execution.
          - Blueprint route [here](https://github.com/evagravin/p4-kangaroos/blob/main/TheSmack/minilabs/app.py#L17-L31), is called in main.py [here](https://github.com/evagravin/p4-kangaroos/blob/main/main.py#L27)
     2. Enhance or Define a Class to manage a complex data set
          - Class is defined [here](https://github.com/evagravin/p4-kangaroos/blob/main/TheSmack/minilabs/ava_minilab.py#L3)
     3. Create an Object from a Class in Python. 
          - Different Objects [here](https://github.com/evagravin/p4-kangaroos/blob/main/TheSmack/minilabs/ava_minilab.py#L4-L31) that calculate mean, median, mode of entered data set
     4. Display data or enhanced data from this Python Object on a Web Page using "getters".
          - Displayed as a table [here](https://github.com/evagravin/p4-kangaroos/blob/main/templates/minilabs/ava-minilab.html#L29-L44) using jinja variables 
     5. Highlight WOW or insight in doing this project. 
          - For my class, I created multiple objects [here](https://github.com/evagravin/p4-kangaroos/blob/main/TheSmack/minilabs/ava_minilab.py#L7-L31) that each do different tasks. There is a function to calcualte the mean, median, and mode, as well as getting the string that the user inputted and sorting it from least to greatest to be displayed on the front end. For the front end, I created an interactive table that allows users to hover over the value and have it pop out a bit more. 

### Risa:
### Eva:
 - Project concept: The user will enter 4 numbers that will be "foiled" as terms in a binomial multiplication expression.
 - Binary Grading:
     1. Use an individual section (blueprint) in your Scrum Team project for Mini Lab definition and execution.
          - Blueprint route [here](https://github.com/evagravin/p4-kangaroos/blob/cc10d4976181095d6b97f846d0bd3ea86b06212b/TheSmack/minilabs/app.py#L39)
     2. Enhance or Define a Class to manage a complex data set
          - Class is defined [here](https://github.com/evagravin/p4-kangaroos/blob/ba99261e1963ed2b0d72c5a558b618919aa6b7ed/TheSmack/minilabs/eva_minilab.py#L1-L10)
     3. Create an Object from a Class in Python. 
          - Object "Foil" [here](https://github.com/evagravin/p4-kangaroos/blob/cc10d4976181095d6b97f846d0bd3ea86b06212b/TheSmack/minilabs/eva_minilab.py#L46) that is the instance of the class and [here](https://github.com/evagravin/p4-kangaroos/blob/222f937e6bc92e625edc699878321a3ecc341582/TheSmack/minilabs/eva_minilab.py#L3-L10) that perform the calculations.
     4. Display data or enhanced data from this Python Object on a Web Page using "getters".
          - Used Getters [here](https://github.com/evagravin/p4-kangaroos/blob/cc10d4976181095d6b97f846d0bd3ea86b06212b/TheSmack/minilabs/eva_minilab.py#L12-L42) and displayed the data with Jinja variables.
     5. Highlight WOW or insight in doing this project. 
          - The class Foil defines the object, or is like a layout for it. It has parameters of the nums, and the numbers that the user enters get passed into it. The terms are made up of those numbers (the certain ones being multiplied to complete the foil process), which are calculated. Then many getters are used to get the data that has already been calculated and the numbers. POST is used to get 4 numbers from the users and renders the template when done. It turns the strings into integers and there is a seperate render template for the page. To display the data, the Jinja variables are used with foil. like foil.num1 and foil.term1 to apply the object foil to them and get the correct output. Also, in the html page, Javascript is used with the "onclick" event, to highlight the displayed equation when clicked. Another button reverts it because it calls the second function which turns the highlight back to transparent. 
      6. full route in app.py file [here](https://github.com/evagravin/p4-kangaroos/blob/22250c4ff8af6b27939b92073b81753d1e0e1408/TheSmack/minilabs/app.py#L39-L49), backend py file [here](https://github.com/evagravin/p4-kangaroos/blob/main/TheSmack/minilabs/eva_minilab.py), html file [here](https://github.com/evagravin/p4-kangaroos/blob/main/templates/minilabs/eva-minilab.html)

### Linda:
## Individual Work Week of 3/26-26

### Ava:
- In Progress (Now Completed) [Story/Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57225859)
- Backlog [Story/Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57744261)
- [Github Commit](https://github.com/evagravin/p4-kangaroos/commit/425ea494f7832df62c3e75edd081d86ab8582ab2) Towards In Progress Story/Ticket
- [Github Commit](https://github.com/evagravin/p4-kangaroos/commit/6a21149482fbf045f9c72e3e286ea1533efe88a9) Toward Mini Lab

### Risa:
- In Progress (Now Completed) [Story/Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57226174)
- Backlog [Story/Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57546949)
- [Github Commit](https://github.com/evagravin/p4-kangaroos/commit/bc9ff513d9388e85d6c92989e10d238d916da396) Towards In Progress Story/Ticket
- [Github Commit](https://github.com/evagravin/p4-kangaroos/commit/0b5f4303f0374b657593720c84095c7e371407ec) Toward Mini Lab

### Eva:
- In Progress (Now Completed) [Story/Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57226156)
- Backlog [Story/Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57748574)
- [Github Commit](https://github.com/evagravin/p4-kangaroos/commit/62f55d2b5c19fab68eb6d3e98d25f48c47b62cde) Towards In Progress Story/Ticket
- [Github Commit](https://github.com/evagravin/p4-kangaroos/commit/a1d8e8622c432b2a4f4ff7926e86750c957d5105) Toward Mini Lab

### Linda:
- In Progress (Now Completed) [Story/Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57458729)
- Backlog [Story/Ticket](https://github.com/evagravin/p4-kangaroos/projects/1#card-57546498)
- [Github Commit](https://github.com/evagravin/p4-kangaroos/blob/main/templates/aboutus.html) Towards In Progress Story/Ticket
- [Github Commit](https://github.com/evagravin/p4-kangaroos/blob/main/templates/minilabs/linda-minilab.html) Toward Mini Lab


### Everyone:
- [Story/Ticket 1](https://github.com/evagravin/p4-kangaroos/projects/1#card-57226374)
- [Story/Ticket 2 - Project Plan](https://github.com/evagravin/p4-kangaroos/projects/1#card-57547049)

## College Board / Teacher Requirements (Track to Meeting Them)

| Big Idea Number / Requirement           | Big Idea Summary  | Project Goal To Meet Each Requirement |
| -------------------------- |---------------------| ----------------------------------|
| Big Idea #1                | Technical Requirements | Backend Code: Flask framework that takes information from both python database files with dictionaries, and sql databases with tables. Utilize libraries, pass variables to html files, and integrate with databases. Have routes for the templates and the main pages (login, homepage, dashboard, form sites).    Database requirements/SQLAlchemy: Use SQLAlchemy to store user information (usernames, passwords, user information). Tables that store the posting information, which will have connections to the user information. Emoji table, which stores the emojis and feelings of the user.|| Big Idea #1                | Technical Requirements | Database requirements/SQLAlchemy: Use SQLAlchemy to store user information (usernames, passwords, user information). Tables that store the posting information, which will have connections to the user information. Emoji table, which stores the emojis and feelings of the user.|
| Big Idea #1                | Technical Requirements | Data-drive UI: User dashboards will be created using data from the user tables. We will create one html page with the template, and use SQL Queries and data-drive UI to create the various unique posts.|
| Big Idea #1                | Technical Requirements | Filtering, searching, and analysing large quantities of data: Will analyze the user information to determine the number of users on the site. Create a search function that searches all trending messages and users on the site. Will search users when creating accounts, and search users when friending other users and sharing your emojis and messages among friends. We’ll also analyze information in the emotions/feelings section as well as messages posted onto the web. We will then create a #trending page so users can see what is trending at the moment.|
| Big Idea #2                | UI Design & Presentation| UI Implementation: We’ll use a styles.css and javascript.js file to implement our styles and animations. Transform and transitions will be used to create animations. Templates will be used to generate the user and playlist pages. We will use HTML, CSS, and Javascript to implement our design.|
| Big Idea #3                | Deployment              | Raspberry Pi Deployment & Internet Routing: The website will be deployed on Eva or Risa’s Raspberry Pi. Port forwarding is already set up. All users will be able to access the website via the Raspberry Pi’s public IP address.|
| Big Idea #3                | Deployment              | Usage of HTTP GET and POST methods: HTTP GET Methods will be used to obtain static web pages such as the homepage, while POST methods will be used to obtain dynamically generated web pages. POST methods will be used on the: Login page and sign up page, Personal user page/pages for other users, Edit user information site, Search.|
