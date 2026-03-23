from setuptools import setup
setup(
    name='cli-anything-drug',
    version='1.0.0',
    packages=['cli_anything.drug'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drug=cli_anything.drug:cli']},
)
