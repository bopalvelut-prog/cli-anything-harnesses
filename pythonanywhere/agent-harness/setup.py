from setuptools import setup
setup(
    name='cli-anything-pythonanywhere',
    version='1.0.0',
    packages=['cli_anything.pythonanywhere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pythonanywhere=cli_anything.pythonanywhere:cli']},
)
