from setuptools import setup
setup(
    name='cli-anything-sake',
    version='1.0.0',
    packages=['cli_anything.sake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sake=cli_anything.sake:cli']},
)
