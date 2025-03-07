from setuptools import setup, find_packages

setup(
    name="HAI_Bot",
    version="0.5",
    license="MIT",
    packages=find_packages(),
    description="A Python package for creating ChatBot with your own data",
    author="Hamed Amiri",
    author_email="your.email@example.com",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HDAI654/HAI_Bot",
    install_requires=["keras", "numpy"],
    classifiers=["Programming Language :: Python :: 3", 
                 "Operating System :: OS Independent",
                 "License :: OSI Approved :: MIT License"
    ],
    package_data={
        'HAI_Bot': ['*.py'],
        'HAI_Bot': ['*.pyi'],
    },
    python_requires='>=3.6',
)