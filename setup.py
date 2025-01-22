from setuptools import setup, find_packages

setup(
    name="vietnamese_conceptizer",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A tool for processing text files and normalizing data using a dictionary",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vietnamese_conceptizer",
    packages=find_packages(),
    package_data={
        "vietnamese_conceptizer": ["data/WORDS_WordNet_And_VCL_ALL_sorted.txt"]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas",
    ],
)
