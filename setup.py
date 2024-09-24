from setuptools import find_packages, setup

# Read the contents of the README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata:
__version__ = "0.0.0"
NAME = "DEI-Decoder"
AUTHOR_USER_NAME = "Ahmed Osman"
AUTHOR_EMAIL = "engineer.ahmedfarouk@gmail.com"

# Setup function to specify package details
setup(
    name= NAME,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "This end-to-end deep learning project aims to classify apple diseases using CNN, MLFlow and DVC.",
    long_description= long_description,
    url= f"https://github.com/Ahmed-Osman-AI/DEI-Decoder",
    project_urls= {
        "Bug Tracker": f"https://github.com/Ahmed-Osman-AI/DEI-Decoder/issues",
    },
    packages= find_packages(),
    install_requires= [],
)
