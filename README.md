StoryBoard Data-Centric Development Project:
=

The purpose of this project is to allow a user to interact with a database using the four basic CRUD functions (Create,
Read, Update, Delete). This database is structured around creating and editing a narrative, be it a more general
worldbuilding exercise, or a more specific story.

This project is designed for people who are writing or planning to write a story, and wish to organise and view their
data, as well as be able to search the data, and to delete, edit or add to the data in question. Navigation is designed
to be as simple as possible, by having a search bar and nesting relevant subcategories on the 'Categories' page (e.g:
'House' and 'City' may show up under the 'Place' section of the 'Categories' page).

UX:
-

This website is designed for storytellers, such as writers or filmmakers. These individuals want to create, structure and
dynamically edit a large amount of information that is relevant to their story, such as 'Characters', 'Places', 'Events'
or 'Chapters'.

The StoryBoard site helps them achieve this via allowing a user to Create, Read, Update and Delete data relevant to their
story (dynamic editing), as well as allowing them to access this information quickly via the navbar links and the search
bar. In addition, the user can create their *own* Categories, Subcategories and Story Elements, allowing a greater
degree of customisability for the user.

### User Stories:

#### User Type 1 - Creating a small, simple story:
* As a user who is creating only a small story, I only want to be able to Create, Access, Edit and Delete parts of my 
story, so that I can structure my story.


#### User Type 2 - Creating a complex or unique story:
* As a user who is creating a complex or unique story, I want to be able to add custom Categories, as well as custom 
Subcategories, that are unique to my story, so that I can better categorize the elements of my story.
* For example, I might be writing a fantasy story, and I might wish to have a category labelled 'Spells', with 
Subcategories such as 'Fire Spell' or 'Healing Spell'.


#### User Type 3 - Not very technologically literate:
* As a user with few technological skills, I need to be able to navigate the site easily, as well as being able 
to get help using or navigating the site *without searching in a search engine*.


#### User Type 4 - Mobile user:
* As a mobile user, I want to be able to access the site on mobile, as well as wanting the site to look good on 
a mobile device, so that I can create my story using a mobile device, instead of a tablet or desktop.


#### User Type 5 - Tablet user:
* As a tablet user, I want to be able to access the site on a tablet, as well as wanting the site to look good on 
a tablet *and* being compatible with a tablet's vertical and horizontal views, so that I can create my story using 
a tablet device, instead of a mobile device or desktop.


Features:
-

### Existing Features:

* Feature 1; Creating Data - Feature 1 allows users of type 1 and 2 to create data, by 
clicking on the 'ADD' buttons in the 'Elements', 'Categories' and 'Subcategories' pages. 
Upon clicking, the user is taken to a form, which they can fill out and then submit, to add 
new Elements, Categories or Subcategories to the database. 
* Feature 2; Reading Data - Feature 2 allows type 1 and 2 users to view their data. Up to 10 
story elements are shown on the homepage, instantly allowing users to see the most recent data 
that has been added. In addition, on the 'Home' page and the 'Elements' page, the users can 
toggle a checkbox in order to choose whether to only see elements which are 'Important' (i.e: 
their 'important' status is set to True in MongoDB). 
Data is displayed in the form of an unordered list, decorated with Materialize's 'collapsible' 
class. On the homepage, this list is an 'accordion', meaning that only one element can be 
expanded at a time (this is to preserve space on the homepage), whereas on the 'Elements', 
'Categories' and 'Subcategories' pages, the list is 'expandable', meaning multiple pieces of 
data can be viewed at once.
On the 'Categories' page, the relevant subcategories are displayed as a collection within each 
list item. For example, a category called 'Places', with subcategories of 'House' and 'City' 
will display those subcategories within its list item.
Finally, the search bar within the nav bar allows users to search for data, and returns 
results relevant to the query, enabling users to quickly search for a specific result.
* Feature 3; Editing Data - Feature 3 allows type 1 and 2 users to edit their data. By clicking
on the 'EDIT' buttons next to a piece of data, the user is taken to a new page, where all of the 
relevant fields are displayed and editable. A user can edit one field, or edit them all, and is 
able to toggle the 'Important' status of elements that they may edit.
* Feature 4; Deletion of Data - Feature 4 allows users of type 1 and 2 to delete their data. 
By clicking on the 'DELETE' button next to a piece of data, the user can permanently delete 
that data from the database.
* Feature 5; Searching for Data - Feature 5 is useful for all 5 users, in different ways. In 
terms of type 1 users, feature 5 allows them to use the search bar, contained within the nav 
bar, to search for pieces of data from the database. This is useful for tasks such as; checking 
if a piece of data has been deleted, checking for accidental duplicates and bringing up all 
pieces of data relevant to a certain term (e.g. 'London').
For type 2 users, their story is complex, and therefore their database is likely to be large. 
By using a search bar, they can search for singular pieces or groups of data. For example, they 
may have a Category called 'Characters' with the Subcategory of 'Good Guys', however for a large 
story, there may be 20+ Story Elements under this subcategory. With a search bar, type 2 users can 
just search for 'London', and immediately see all characters with 'London' in their 'Name' or 
'Vignette' fields.
For type 3 users, a search bar makes for minimal navigation, as the user can simply search for 
what they want. For example, if a type 3 user is confused as to how they can find a piece of data 
called 'Cars', they can simply search for that data.
For type 4 and 5 users, the screens of tablets and mobiles are much smaller than those of desktops. 
For this reason, a search bar makes for better UX, as it decreases user reliance on buttons, instead 
allowing the user to navigate through the site with a much larger, 'search bar' element.
* Feature 6; Viewing Important Data Only - Feature 6 is useful primarily for type 2 and 3 users. 
For type 2 users, being able to only view important elements allows allows them to slim down the number 
of elements they are presented with to only what is most relevant for the story.
For type 3 users, being able to only view important elements allows them to have less information on 
the screen, meaning that they are less likely to be confused and/or overstimulated.
* Feature 7; Toggling Important Data - Feature 7 is useful for type 1 and 2 users, as it allows them 
to edit the 'Important' status of elements without having to go to the trouble of loading the 'edit' 
page. This is not a massive feature, but does make for better UX by allowing simple editing to be done 
without clicking the 'EDIT' button.
* Feature 8; 404 Error Handling - Feature 8 is useful for ALL users, but especially for type 3 users. 
The 404.html page provides a quick explaination of the problem 'Page Not Found', as well as providing a 
link to the Homepage, as well as an email address for the purposes of complaints or feedback. This will 
be most useful for type 3 users, as they are the least likely to understand what a 404 error is, and will 
need clear direction to navigate back to the Homepage.
* Feature 9; Mobile & Tablet compatibility - Feature 9 is useful for type 4 and 5 users. By using a mobile-
first design, coupled with @media() rules for both tablets *and* mobiles as well as Materalize 
[tabs](http://archives.materializecss.com/0.100.2/tabs.html) that display in the Navbar on mobiles and 
tablets, the site is easy to navigate on these screen sizes.
* Feature 10; Help Page - Feature 10 is useful for type 3 users. By providing a list of clear instructions 
on how to use the site, type 3 users are able to navigate the site by consulting the 'Help' page.


### Features Left to Implement:

* Ability to log in and create an account.
* Handling of other errors (e.g. 403).
* Ability to have multiple stories or narratives that a user can switch between.


Technologies used:
-
* [Materalize](http://archives.materializecss.com/0.100.2/) was used for HTML, CSS and JavaScript classes.
* [jQuery](https://jquery.com/) was used in the JavaScript code.
* [Logo Makr](https://logomakr.com/) was used to create the favicon and the navbar logo.
* [Font Awesome](https://fontawesome.com/) was used to display the social media icons in the footer.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/)
were used to help connect and send commands to MongoDB.
* [The MongoDB Atlas](https://www.mongodb.com/cloud/atlas) was used to store site data.
* [Heroku](https://www.heroku.com) was used to render the site.
* [Github](https://github.com/) was used to store the site's code in a repository.

Testing:
-

AUTOMATED TESTING

Deployment:
-

TALK ABOUT THE TROUBLES WITH THE 'IMPORTANT' TOGGLES

TALK ABOUT SETTING UP THE JAVASCRIPT FOR THE ELEMENT EDITOR (THE AUTOCORRECTOR)

This project is deployed to GitHub pages, and can be viewed in its rendered form in Heroku [here](https://story-database-milestone.herokuapp.com/). 
It can also be viewed in its code form in github [here](https://github.com/Felix-Redwood/Data-Centric-Development-Milestone-Project).

I have taken steps to ensure that after every session with the development version of this project, I push my code to both Github and Heroku.
Currently there is no difference between the deployed version of this project and the development version.

Credits:
-

Content:

* The CSS stylings, and many HTML elements, of this site, were taken from the [Materialize v0.100.2 CDN](http://archives.materializecss.com/0.100.2/about.html).


Media:

* [Logo Makr](https://logomakr.com/) was used to create the site's images.


Acknowledgements:

* I gained the coding knowledge neccesary to make this site from the [Code Institute](https://codeinstitute.net/), Dublin.