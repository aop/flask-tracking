from distutils.core import setup

files = ["flask_tracking/*"]

setup(name = "flask_tracking",
    version = "1",
    description = "Logs Flask requests and responses to MongoDB",
    author = "Oskari Petas",
    author_email = "oskari.petas@gmail.com",
    url = "http://oskaripetas.fi",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['flask_tracking'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'package' : files },
    #long_description = """Really long text here.""" 
    install_requires=['mongoengine>=0.8']
) 
