from setuptools import setup
setup(
    name='cli-anything-brocade',
    version='1.0.0',
    packages=['cli_anything.brocade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brocade=cli_anything.brocade:cli']},
)
