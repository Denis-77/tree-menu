# tree-menu
- Rendering each menu requires exactly 1 request to the database!
- The menu is implemented using a "template tag"
- Everything above the selected item is expanded. The first level of nesting under the highlighted item is also expanded.
- Stored in the database.
- Editable in the standard Django-admin panel.
- The active menu item is determined based on the URL of the current page.
- There can be several menus on one page. They are identified by their name.
- When you click on the menu, you go to the URL specified in it.
