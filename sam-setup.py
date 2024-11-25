from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sam-lang",
    version="0.1.0",
    author="@EthicalGod",
    author_email="admin@ethicalgod.tech",
    description="Sam Programming Language - A friendly language wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samfckz69/sam-lang",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'sam=sam_lang.cli:main',
        ],
    },
    install_requires=[
        'click>=7.0',
        'colorama>=0.4.4',
        'prompt_toolkit>=3.0.0',
    ],
)
