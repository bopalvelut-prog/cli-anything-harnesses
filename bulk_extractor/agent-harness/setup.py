from setuptools import setup
setup(
    name='cli-anything-bulk_extractor',
    version='1.0.0',
    packages=['cli_anything.bulk_extractor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bulk_extractor=cli_anything.bulk_extractor:cli']},
)
