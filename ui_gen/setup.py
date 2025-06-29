from setuptools import setup, find_packages

setup(
    name="ui-gen",
    version="0.1.0",
    author="Nazar Lenyshyn",
    author_email="nleny@softserveinc.com",
    packages=find_packages(),
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "ui-gen=cli.main:ui_gen_group",
        ],
    },
)