# Flask-MongoDB Web App

## The Cat Database

For this project, I decided to create a web application that has information about 27 different breeds of cats. Users can use a search bar to type in the name of a particular cat, or they can use the buttons on the home page to navigate to the page of a particular breed. It should be noted that to correctly use the search bar, the user must correctly spell the breed's name and capitalize the first letter, and add any special characters if necessary. For instance, if a user wants to search for the Balinese-Javanese, they would need to type in "Balinese-Javanese" exactly.

Once on the web page for a particular breed, users will be greeted by a page displaying the name of the breed, an image of the breed, and a short description. They can use a button to navigate back to the home page, or edit/delete the existing description of a particular cat. If they want to restore this description, they can use the restore button.

Here is the link to [the website](https://i6.cims.nyu.edu/~aa8690/web-app-aa8690/flask.cgi/home)

## Problems With the Website

Although my website ran well when I was trying to set things up locally, I encountered many problems after publishing my website to the NYU CS Department's web server. For one, the search function no longer works. Additionally, there is missing data for certain cats. For example, although my csv data has data for the breed, "Abyssinian", when one clicks the link for "Abyssinian" on the website, it does not redirect them to the correct page. The final problem is that the "restore" button no longer works. Originally, if a description for a certain breed was edited or deleted, a restore button would appear on that cat breed's page that would restore the description to the original description. This button no longer works. I suspect this is because I had issues getting the redirect function to work with the updated links, which is very unfortunate since it worked when I was testing the website locally. Regardless, my website still performs create, read, update, and delete functions. 
