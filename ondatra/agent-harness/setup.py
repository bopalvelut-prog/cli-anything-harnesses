from setuptools import setup
setup(
    name='cli-anything-ondatra',
    version='1.0.0',
    packages=['cli_anything.ondatra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ondatra=cli_anything.ondatra:cli']},
)
