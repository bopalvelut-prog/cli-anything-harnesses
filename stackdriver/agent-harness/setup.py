from setuptools import setup
setup(
    name='cli-anything-stackdriver',
    version='1.0.0',
    packages=['cli_anything.stackdriver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stackdriver=cli_anything.stackdriver:cli']},
)
