# Django_Fluxome_Database

FLUXOME DATABASE PROJECT README FILE
------------------------------------
This file contains basic guidance on the Fluxome Database project.
The directory contains the following files:
- data_1_filtered.csv
- data_2_filtered.csv
- data_3_filtered.csv
- name_map.csv
- project.db
- my.cnf
- flux (folder)
- the README file itself

The name_map.csv file contains the mapping information for flux reactions. As reactions can be represented by different names in different research papers, there is a need for a unique identification ID. Note that both the description and database name columns should be present too in each dataset in the database.

The project.db file contains the current MySQL database state for the project. Information to access the database (database name, username, password, default character setting) is contained in the my.cnf file. The path to the my.cnf file should be provided in the DATABASES section of the settings.py file in the Django project folder.

The Django project directory ("flux") contains all the relevant Django files and folders.


DATABASE
------------------------------------
Currently, the fluxome database contains two tables (other than the tables automatically created as a result of connecting the database file to Django) - queries_flux and queries_flux2. They correspond to the first and second filtered datasets respectively.

To add a new dataset to the Django project, add a new model to the models.py file in the project directory. The data must be preprocessed beforehand (see the DATA FORMAT section below for instructions). One can access the database records either directly with the MySQL client or through the Django Python interface in the terminal window. 

Run "/usr/local/mysql/bin/mysql -u root -p" in the terminal window to access the MySQL interface. Make sure to install the client first by running "pip install mysqlclient". Instructions to run the Django Python interface in the terminal window can be found in the Django documentation online.


DATA FORMAT
------------------------------------
The three .csv files currently present in the directory are styled based on a standardized format. Each .csv file must contain the following columns: "flux_name", "description", "db_name", and "reaction_id". The only column ordinarily present in the data found in research papers is "flux_name", so other columns need to be added and standardized across datasets using the "name_map.csv" helper file.

The "reaction_id" column is meant to serve as a primary key for each of the datasets. The values must be unique for each reaction in the database so that it is possible to fetch data from multiple tables at once by writing JOIN queries.

Another requirement is that column names are in lowercase, with individual words separated by underscores. Entries in non-numeric columns often contain extra leading and trailing zeros which should be removed in the filtering process. These changes can be made by writing Python code or manually in .csv editors (like Microsoft Excel), depending on the size of the dataset. It is difficult to come up with a single data preprocessing script as the data found online are often initially in different formats.

Data Source 1 - https://onlinelibrary.wiley.com/doi/10.1111/tpj.12252

Data Source 2 - http://www.plantphysiol.org/content/148/2/704/tab-figures-data

Data Source 3 - https://www-sciencedirect-com.libproxy1.nus.edu.sg/science/article/pii/S1096717610000510


DJANGO ESSENTIAL FILES AND OPERATIONS
------------------------------------

The Django version used in this project is 3.1.

1. settings.py

This is a place to add new apps if they are created within the Django project. Apart from that, it contains the path to the database configuration file. Place the "my.cnf" configuration file on a local machine and provide the path to it in the relevant section of the DATABASES dictionary. When working with design, provide the path to the static CSS files in STATIC_URL and STATICFILES_DIRS.

2. urls.py (both global and within the 'queries' app)

This is a place to work with the links to HTML templates found within the project. So far, the project only contains two pages - home and "/queries/". The "/queries/" directory contains a search form and sample flux entries. By clicking on hyperlinks produced as a result of search queries, one can see more detailed information about each individual reaction. To extend project functionality and add new pages, create more HTML templates and place them in the "templates" folder. After that, make relevant changes to the "urls.py" file to establish the desired relationship between HTML templates.

3. models.py

As mentioned earlier, new datasets can be added by creating more models in this file. Existing models can be altered too. After making changes to the model classes and changing to the project directory in the terminal window, run "python manage.py makemigrations" and then "python manage.py migrate" for the changes to take effect. It is easier to create models from scratch though, as there might be some difficulties with providing default values for newly added fields.

4. views.py

This project makes use of function-based views to collect data from and pass it to HTML templates. The "index" function in particular accepts an argument from the search form and contains SQL queries to search the first and second datasets separately. Changes can be made to combine these queries into one. However, the newest versions of the filtered datasets need to be uploaded first. Custom SQL queries should be written here. It is also possible to collect data from various forms in the HTML templates and use it to filter SQL query results.

5. static.py

This file contains the CSS design settings. As of now, the project utilizes a basic Bootstrap template available at https://startbootstrap.com/template/simple-sidebar. More elaborate design templates can be found on the same website or elsewhere online. For further user interaction features, JavaScript functionality can be added in the future.

6. admin.py

This file determines which models are available for editing from the administrator side of the project. The admin interface can be accessed at "/admin/". Users can be created in the terminal window. Database records can be created, deleted, or altered from the admin side. See the Django documentation (version 3.1) for additional functionality.


GENERAL PROJECT FUNCTIONALITY AND POTENTIAL IMPROVEMENTS
------------------------------------
As of now, the project allows one to search flux reactions by flux name and description. Flux name has to be stated exactly, whereas the descriptions will be searched for partial matches too. 5 sample entries are also displayed under the search form for the user to have an understanding of the kind of data contained in the tables. The filters currently available next to the search form are placeholders - their functionality can be added at a later point.

In the future, it would be a significant improvement to standardize data preprocessing, although the data found online are so diverse that it hardly appears realistic. Apart from that, deeper subject knowledge needs to be utilized to add relevant filters to be able to search the data more efficiently. Another useful feature would be for users to be able to submit their own entries as an addition to the existing database. Hopefully, this app could form a basis for further research in the area and enable more active collaboration in the fluxome research community.


ACKNOWLEDGMENTS
------------------------------------
Tutorials used while setting up the Django functionality of the project:

https://www.youtube.com/watch?v=NbsRVfLCE1U

https://www.youtube.com/watch?v=SNyCV8vOr-g

https://www.youtube.com/watch?v=F5mRW0jo-U4

https://docs.djangoproject.com/en/3.1/

https://www.geeksforgeeks.org/rendering-data-frame-to-html-template-in-table-view-using-django-framework/

Special thanks to Professor Maurice Cheung of Yale-NUS College for the support and guidance in this project.



