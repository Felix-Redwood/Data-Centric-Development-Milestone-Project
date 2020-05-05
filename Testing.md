

#### Automated Testing:

'Elements' on the site are called 'story_elements' within the database. Almost every field within each element has a 
type of 'text', however the 'important' field is a boolean, and so has a type of 'bool'. Within the 
'toggle\_element\_important\_home' and the 'toggle\_element\_important_elements' functions in the run.py file, 
the *assert* method has been used, which checks if the 'important' field has a type of 'bool'. If the field does 
not have this type, an error is returned, informing us of this.
<br>
In addition, the 'update_element' function also uses the *assert* method to ensure that a variable called 'important' 
within the function is a boolean.



#### Manual Testing - Create:

* Creating a new Element:
    1. Go to the 'Elements' page and click the 'NEW ELEMENT' button.
    2. Try to add an Element without providing the name and verify that an error message appears.
    3. Try to add an Element without providing the vignette and verify that an error message appears.
    4. Try to add an Element without providing the category name and verify that an error message appears.
    5. Try to add an Element without providing the subcategory name and verify that an error message appears.


* Creating a new Category:
    1. Go to the 'Categories' page and click the 'NEW CATEGORY' button.
    2. Try to add a Category without providing the name and verify that an error message appears.
    3. Try to add a Category without providing the description and verify that an error message appears.


* Creating a new Subcategory:
    1. Go to the 'Subcategories' page and click the 'NEW SUBCATEGORY' button.
    2. Try to add a Subcategory without providing the category and verify that an error message appears.
    2. Try to add a Subcategory without providing the name and verify that an error message appears.
    3. Try to add a Subcategory without providing the description and verify that an error message appears.



#### Manual Testing - Read:

* Reading an Element from the Homepage:
    1. Go to the Homepage and click on the Element.
    2. Verify that the Element's 'vignette' and 'important' fields are shown in a collapsible list.


* Reading an Element from the 'Elements' page:
    1. Go to the 'Elements' page and click on the Element.
    2. Verify that *all* of the Element's fields are shown in a collapsible list.


* Reading a Category:
    1. Go to the 'Categories' page and click on the Category.
    2. Verify that *all* of the Category's fields are shown in a collapsible list.
    3. Verify that, within that list, the all relevant Subcategories are shown.


* Reading a Subcategory:
    1. Go to the 'Subcategories' page and click on the Subcategory.
    2. Verify that *all* of the Subcategory's fields are shown in a collapsible list.



#### Manual Testing - Update:

* Updating an Element from the Homepage:
    1. Go to the Homepage and click the 'EDIT' button next to the element.
    2. Verify that all relevant information from the element occupies each section of the form (e.g; the 
    'Name' field contains the Element's name).
    2. Try to update an Element without the 'name' field filled and verify that an error message appears.
    3. Try to update an Element without the 'vignette' field filled and verify that an error message appears.
    4. Try to update an Element without a selected 'category' and verify that an error message appears.
    5. Try to update an Element without a selected 'subcategory' and verify that an error message appears.


* Toggling an Element's 'important' status from the Homepage:
    1. Go to the Homepage and click on the Element.
    2. Verify that a toggle with the label 'important' appears in the Element's dropdown as well as a button 
    labelled 'toggle'.
    2. Try to switch the toggle without clicking the button and verify that no error occurs.
    3. Switch the toggle and click on the 'toggle' button and verify that the page reloads, and the 'important' 
    label in the Element's dropdown is now the opposite of what it was (e.g; if it was checked, it is now 
    unchecked).


* Updating an Element from the 'Elements' Page:
    1. Go to the 'Elements' page and click the 'EDIT' button next to the Element.
    2. Verify that all relevant information from the Element occupies each section of the form (e.g; the 
    'Name' field contains the Element's name).
    2. Try to update the Element without the 'name' field filled and verify that an error message appears.
    3. Try to update the Element without the 'vignette' field filled and verify that an error message appears.
    4. Try to update the Element without a selected 'category' and verify that an error message appears.
    5. Try to update the Element without a selected 'subcategory' and verify that an error message appears.


* Toggling an Element's 'important' status from the 'Elements' page:
    1. Go to the 'Elements' page and click on the Element.
    2. Verify that a toggle with the label 'important' appears in the Element's dropdown as well as a button 
    labelled 'toggle'.
    2. Try to switch the toggle without clicking the button and verify that no error occurs.
    3. Switch the toggle and click on the 'toggle' button and verify that the page reloads, and the 'important' 
    label in the Element's dropdown is now the opposite of what it was (e.g; if it was checked, it is now 
    unchecked).


* Updating a Category:
    1. Go to the 'Categories' page and click the 'EDIT' button next to the Category.
    2. Verify that all relevant information from the Category occupies each section of the form (e.g; the 
    'Name' field contains the Category's name).
    2. Try to update the Category without the 'name' field filled and verify that an error message appears.
    3. Try to update the Category without the 'description' field filled and verify that an error message appears.


* Updating a Subcategory:
    1. Go to the 'Subcategories' page and click the 'EDIT' button next to the Subcategory.
    2. Verify that all relevant information from the Subcategory occupies each section of the form (e.g; the 
    'Name' field contains the Subcategory's name).
    2. Try to update the Subcategory without the 'name' field filled and verify that an error message appears.
    3. Try to update the Subcategory without the 'description' field filled and verify that an error message appears.
    4. Try to update the Subcategory without a selected 'category' and verify that an error message appears.



#### Manual Testing - Delete:

* Deleting an Element from the Homepage:
    1. Go to the Homepage and click the 'DELETE' button next to the Element.
    2. Verify that the Homepage reloads, and the Element is no longer displayed.
    3. Go to the Homepage and use Google Developer Tools to resize the screen to that of a phone.
    4. Verify that, instead of the button reading 'DELETE' it reads 'DEL'.
    5. Click on the 'DEL' button next to the Element.
    6. Verify that the Homepage reloads, and the Element is no longer displayed.


* Deleting an Element from the 'Elements' Page:
    1. Go to the 'Elements' page and click the 'DELETE' button next to the Element.
    2. Verify that the 'Elements' page reloads, and the Element is no longer displayed.
    3. Go to the 'Elements' page and use Google Developer Tools to resize the screen to that of a phone.
    4. Verify that, instead of the button reading 'DELETE' it reads 'DEL'.
    5. Click on the 'DEL' button next to the Element.
    6. Verify that the 'Elements' page reloads, and the Element is no longer displayed.


* Deleting a Category:
    1. Go to the 'Categories' page and click the 'DELETE' button next to the Category.
    2. Verify that the 'Categories' page reloads, and that the Category is no longer displayed.
    3. Go to the 'Categories' page and use Google Developer Tools to resize the screen to that of a phone.
    4. Verify that, instead of the button reading 'DELETE' it now reads 'DEL'.
    5. Click on the 'DEL' button next to the Category.
    6. Verify that the 'Categories' page reloads, and the Category is no longer displayed.


* Deleting a Subcategory:
    1. Go to the 'Subcategories' page and click the 'DELETE' button next to the Subcategory.
    2. Verify that the 'Subcategories' page reloads, and that the Subcategory is no longer displayed.
    3. Go to the 'Subcategories' page and use Google Developer Tools to resize the screen to that of a phone.
    4. Verify that, instead of the button reading 'DELETE' it now reads 'DEL'.
    5. Click on the 'DEL' button next to the Subcategory.
    6. Verify that the 'Subcategories' page reloads, and the Subcategory is no longer displayed.



#### Manual Testing - Search:

* Searching for an Element:
    1. In the Search Bar, located in the Navbar, type in the name of the Element.
    2. Press enter, or click the button with the magnifying glass icon next to the Search Bar.
    3. Verify that the relevant Elements show up under the 'Elements' header in the Search Results page.
    4. Click on the Element and verify that you are taken to a page to edit the Element.
    5. Verify that all the information on the 'Edit' page is correct.


* Searching for a Category:
    1. In the Search Bar, located in the Navbar, type in the name of the Category.
    2. Press enter, or click the button with the magnifying glass icon next to the Search Bar.
    3. Verify that the relevant Categories show up under the 'Categories' header in the Search Results page.
    4. Click on the Category and verify that you are taken to a page to edit the Category.
    5. Verify that all the information on the 'Edit' page is correct.


* Searching for a Subcategory:
    1. In the Search Bar, located in the Navbar, type in the name of the Subcategory.
    2. Press enter, or click the button with the magnifying glass icon next to the Search Bar.
    3. Verify that the relevant Subcategories show up under the 'Subcategories' header in the Search Results page.
    4. Click on the Subcategory and verify that you are taken to a page to edit the Subcategory.
    5. Verify that all the information on the 'Edit' page is correct.


* Searching for data which isn't there:
    1. In the Search Bar, located in the Navbar, type in the name of the nonexistent data item.
    2. Press enter, or click the button with the magnifying glass icon next to the Search Bar.
    3. Verify that, under the relevant header, there are no data items, and that, under that header, 
    there is a small message verifying that there are no data items that match the search.
    4. For example; if you were to search for an Element which didn't exist, you would verify that, 
    under the 'Elements' header, there were no results, and instead there was a small message stating 
    "There are no Elements matching that search"



#### Manual Testing - 404 error:

* Purposefully navigating to a nonexisting page:
    1. In the URL, type in a pathway that does not exist (e.g. /nopath).
    2. Verify that you are redirected to a 404 error page with a link back to the Homepage.
    3. Click the link, and verify that you are taken back to the Homepage.
    4. Navigate back to the 404 page, click the 404 image and verify that youa re taken 
    back to the Homepage.

* Navigating to a nonexisting page on Mobile or Tablet:
    1. In the URL, type in a pathway that does not exist (e.g. /nopath).
    2. Verify that you are redirected to a 404 error page with a link back to the Homepage.
    3. Use Google Developer Tools to view the page on a Mobile, a vertical Tablet and a 
    horizontal Tablet screen.
    4. Verify that, on a Mobile screen, there is *no* 404 image, and that the link takes you 
    back to the Homepage.
    5. Verify that, on a vertical Tablet screen, there is *no* 404 image, and that the link 
    takes you back to the Homepage.
    6. Verify that, on a horizontal Tablet screen, there *is* a 404 image, and that the link takes you 
    back to the Homepage.
    7. Verify that, on a horizontal Tablet screen, clicking the 404 image returns you to the Homepage.



#### Manual Testing - Mobile/Tablet compatibility:

* Testing Mobile compatability:
    1. Go to the Homepage, and use Google Developer tools to view the site through a mobile 
    screen. 
    2. Verify that the Navbar now consists of two tiers; the first containing the logo (without text) 
    and the Search Bar, the second containing 3 tabs, each labelled 'Elements', 'Categories' and 
    'Subcategories' respectively.
    3. Tap on the 'Toggle Important' lever on the homepage and verify that, when the lever is 'on', 
    you only see Elements which are 'Important' and, when the lever is 'off', you see *all* Elements.
    4. Tap on the 'DEL' button next to an Element and verify that the page reloads and the Element 
    is gone.
    5. Tap on the 'EDIT' button next to an Element and verify that you are taken to the 'Edit' page 
    for that Element, and that all of the information in the fields is correct.
    6. Tap on the 'Elements' tab and verify that you are taken to the 'Elements' page.
    7. Tap on the 'Toggle Important' lever and verify that, when the lever is 'on', you only 
    see Elements which are 'Important' and, when the lever is 'off', you see *all* elements.
    8. Tap on the 'DEL' button next to an Element and verify that the page reloads and the Element 
    is gone.
    9. Tap on the 'EDIT' button next to an Element and verify that you are taken to the 'Edit' page 
    for that Element, and that all of the information in the fields is correct.
    10. Tap on the 'NEW ELEMENT' button at the bottom of the screen and verify that you are taken to 
    the 'Add' page, and that if you fill in the form, you are returned to the 'Elements' page and 
    the new Element is displayed (with this, verify that you are unable to send a form without providing 
    a 'Name', 'Vignette', 'Category' and 'Subcategory' for the Element).
    11. Tap on the 'Categories' tab and verify that you are taken to the 'Categories' page.
    12. Tap on the 'DEL' button next to a Category and verify that the page reloads and the Category 
    is gone.
    13. Tap on the 'EDIT' button next to a Category and verify that you are taken to the 'Edit' page 
    for that Category, and that all of the information in the fields is correct.
    14. Tap on the 'NEW Category' button at the bottom of the screen and verify that you are taken to 
    the 'Add' page, and that if you fill in the form, you are returned to the 'Categories' page and 
    the new Category is displayed (with this, verify that you are unable to send a form without providing 
    a 'Name' and 'Description' for the Category).
    15. Tap on the 'Subcategories' tab and verify that you are taken to the 'Subcategories' page.
    16. Tap on the 'DEL' button next to a Subcategory and verify that the page reloads and the Subcategory 
    is gone.
    17. Tap on the 'EDIT' button next to a Subcategory and verify that you are taken to the 'Edit' page 
    for that Subcategory, and that all of the information in the fields is correct.
    18. Tap on the 'NEW Subcategory' button at the bottom of the screen and verify that you are taken to 
    the 'Add' page, and that if you fill in the form, you are returned to the 'Subcategories' page and 
    the new Subcategory is displayed (with this, verify that you are unable to send a form without providing 
    a 'Name', 'Description' and 'Category' for the Subcategory).
    19. Tap on the Search Bar in the Navbar, write a query and press the button with the magnifying glass 
    icon. Verify that the relevant results are returned under the relevant headers. Verify that, when 
    tapped, these results send you to the 'Edit' page for that results.
    20. Finally, verify that, when an invalid query is made, no data is returned, and there is a message 
    under the relevant headers informing you that nothing matches your search.


* Testing Tablet compatibility:
    1. Go to the Homepage, and use Google Developer tools to view the site through a tablet 
    screen.
    3. Tap on the 'Toggle Important' lever on the homepage and verify that, when the lever is 'on', 
    you only see Elements which are 'Important' and, when the lever is 'off', you see *all* Elements.
    4. Tap on the 'DELETE' button next to an Element and verify that the page reloads and the Element 
    is gone.
    5. Tap on the 'EDIT' button next to an Element and verify that you are taken to the 'Edit' page 
    for that Element, and that all of the information in the fields is correct.
    6. Tap on the 'Elements' link in the Navbar and verify that you are taken to the 'Elements' page.
    7. Tap on the 'Toggle Important' lever and verify that, when the lever is 'on', you only 
    see Elements which are 'Important' and, when the lever is 'off', you see *all* elements.
    8. Tap on the 'DELETE' button next to an Element and verify that the page reloads and the Element 
    is gone.
    9. Tap on the 'EDIT' button next to an Element and verify that you are taken to the 'Edit' page 
    for that Element, and that all of the information in the fields is correct.
    10. Tap on the 'NEW ELEMENT' button at the bottom of the screen and verify that you are taken to 
    the 'Add' page, and that if you fill in the form, you are returned to the 'Elements' page and 
    the new Element is displayed (with this, verify that you are unable to send a form without providing 
    a 'Name', 'Vignette', 'Category' and 'Subcategory' for the Element).
    11. Tap on the 'Categories' link in the Navbar and verify that you are taken to the 'Categories' page.
    12. Tap on the 'DELETE' button next to a Category and verify that the page reloads and the Category 
    is gone.
    13. Tap on the 'EDIT' button next to a Category and verify that you are taken to the 'Edit' page 
    for that Category, and that all of the information in the fields is correct.
    14. Tap on the 'NEW Category' button at the bottom of the screen and verify that you are taken to 
    the 'Add' page, and that if you fill in the form, you are returned to the 'Categories' page and 
    the new Category is displayed (with this, verify that you are unable to send a form without providing 
    a 'Name' and 'Description' for the Category).
    15. Tap on the 'Subcategories' link in the Navbar and verify that you are taken to the 'Subcategories' page.
    16. Tap on the 'DELETE' button next to a Subcategory and verify that the page reloads and the Subcategory 
    is gone.
    17. Tap on the 'EDIT' button next to a Subcategory and verify that you are taken to the 'Edit' page 
    for that Subcategory, and that all of the information in the fields is correct.
    18. Tap on the 'NEW Subcategory' button at the bottom of the screen and verify that you are taken to 
    the 'Add' page, and that if you fill in the form, you are returned to the 'Subcategories' page and 
    the new Subcategory is displayed (with this, verify that you are unable to send a form without providing 
    a 'Name', 'Description' and 'Category' for the Subcategory).
    19. Tap on the Search Bar in the Navbar, write a query and press the button with the magnifying glass 
    icon. Verify that the relevant results are returned under the relevant headers. Verify that, when 
    tapped, these results send you to the 'Edit' page for that results.
    20. Finally, verify that, when an invalid query is made, no data is returned, and there is a message 
    under the relevant headers informing you that nothing matches your search.


##### How the project looks on different screen sizes:


This project *works* in essentially in the same way in *all* browsers and screen sizes. All buttons lead to the same page. 
There are, however, various visual and aesthetic differences. For one, on smaller screens, the '404' image on the '404' 
page will not show up, so as to conserve space. As well as this, the 'DELETE' buttons will say 'DEL' on mobile devices, 
once again to save space.

Finally, in the Navbar, the 'Elements', 'Categories' and 'Subcategories' sections show up as materialize 
[tabs](http://archives.materializecss.com/0.100.2/tabs.html) instead of simple Navbar links, and in the footer, the 
'about' section and the social-media icons do not show up on mobile devices.

Beyond this, the project is largely simillar on different screen sizes. Em is used instead of pixels in *all* custom 
CSS, to ensure that the project scales well with screen size.


#### A bug in the Project - 'Important' Toggles:


On the Homepage and the 'Elements' page, there is a toggle within each Element's dropdown. For this project, I wanted 
users to be able to toggle an Element's 'important' status without having to enter the 'Edit' page. I wanted this to 
be the case because I presumed that toggling the 'important' status of an element would occur more often than editing 
other parts of an element, and so I wanted a user to be able to toggle 'important' without too much unnessecary navigation. 

The error occured in my function in my run.py file. Initially, I attempted to use 
JavaScript so that when the 'important' tag of an element was toggled, the page would reload and update the element, 
changing it's 'important' status (If the element *was* important, it would become *not* 'important', and vice versa). 

I did this by assigning the class of "importantSwitch" to the 'important' levers, and using the following JavaScript:

$(".importantSwitch").on("change", "input:checkbox", function() {
$(".importantSwitch").submit();
});

However, upon clicking the 'important' lever next to an element, I was met with an error page, stating:

###### TypeError: 'Cursor' object is not callable.


In my 'toggle\_element\_important_elements' function in run.py, I set a variable called importantbool, used in the function 
to determine whether the 'important' lever was checked or not. My code at this time for generating importantbool was:

importantbool = mongo.db.story\_elements.find({'\_id': ObjectId(element_id)})

And my code to determine if 'important' was True was:

if importantbool({"important": True}):

The issue, however, was that the 'importantbool' variable was an *entire* entry from my database, so I proceeded to change the 
code to:

if importantbool['important'] == True:

Doing this, however, resulted in me recieving a different error page upon clicking the 'important' lever, with the message:

###### TypeError: index 'important' cannot be applied to Cursor instances.


To help identify the problem, I added a print() statement in my function, that printed 'importantbool' to the console. 
Upon doing this, the console printed (<\\pymongo.cursor.Cursor object at 0x7f52e53c75f8>). This means that 'importantbool' was 
a 'cursor' type, meaning that more than one database entry was returned from the function. To fix this, I replaced '.find()' 
in my function with .find_one(), resulting in the code for generating 'importantbool' looking like this:

importantbool = mongo.db.story\_elements.find\_one({'\_id': ObjectId(element_id)})

I then clicked on each element's 'toggle important' lever. The expectation was that, upon each click, the element's 'element_id' 
would be printed to the console, however no matter what element's lever I clicked, they each printed the same 'element_id' to the 
console (That of an element called "Gus' house"). This meant that each element was loading with the same 'element_id', suggesting 
that there was a problem with the HTML code, rather than the Python code.

I then rendered the 'elements' page and used Google Developer Tools to confirm that each element was loading with the same 'element_id'.

Within my 'home.html' file, I was attempting to use Flask to generate a 'checked' lever for the element if the element was 'important' 
and an 'unchecked' lever if the element wasn't 'important. I used this code to achieve this:

 {% if element.important %}
    HTML for a checked lever.
 {% else %}
    HTML for an unchecked lever.
 {% endif %}

However, I realised that {% if element.important %} was only checking if the element had a *value* for 'important' (which all 
elements did), not if that value was *True* or not.

I changed the code to:

HTML for a lever
<\\input {% if element.important == True %}checked{% endif %}>

This served to both simplify the code, as I no longer needed HTML code for both a checked *and* unchecked lever (I only needed 
the code for the *checked* attribute itself to change), as well as to *actually* target the status of 'important'.

At this stage, upon clicking the lever to run the 'toggle\_element\_important_elements' function, I could see in the console 
that the 'element_id' being used for the URL of the function was different from the one that was being returned from the 
database. The reason for this was my earlier JavaScript:

$(".importantSwitch").on("change", "input:checkbox", function() {
$(".importantSwitch").submit();
});

What this javascript meant was that, whenever the lever with the class of "importantSwitch" was clicked (which triggered the 
"change" portion of the function), it submitted the data for *all* of the switches on the webpage, including *all* of the 
'element\_id' data for all of the elements. 'importantbool' was assigned the 'element_id' of the first element in the list 
of data.

After doing this (And fixing a bad syntax in the function where I used updateOne instead of update_one), the buttons worked.