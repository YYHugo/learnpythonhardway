try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    # Still I don't know what it does
    'description': 'Trying to get arguments and print',
    # Shows  at python doc (command 'pydoc' or help()) authors
    'author': 'Hugo',
    'url': 'nowhere',
    'download_url': 'Where to download it.',
    'author_email': 'hugoh@cpqd.com.br',
    'version': '0.1',
    'install_requires': ['nose'],
    # Name the folder where your Python modules are
    # (If you have other packages (dirs) or modules (py files) then put them
    # into the package directory 'package_dir'- they will be found  recursively
    'packages': ['printARGS'],
    'scripts': ['bin/jesusMYscript'],
    'long_description': "Really long text here. Trying to get arguments"
                        "and print",
    'name': 'projectname'
}

# Runs with the dictionary above 'config' as argument
setup(**config)
