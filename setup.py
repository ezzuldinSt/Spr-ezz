
import setuptools

setuptools.setup(
    name='Spr-ezz',  
    version='0.1',
    author="Spr3z",
    author_email="zezo.665.5@gmail.com",
    description="hello pypi :)",
    long_description="hello pypi :)",
    url="https://github.com/ezzuldinSt/Spr-ezz",
    packages=["Spr-ezz"],
    entry_points = {
        "console_scripts": ['Spr-ezz = Spr-ezz.Spr-ezz:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
