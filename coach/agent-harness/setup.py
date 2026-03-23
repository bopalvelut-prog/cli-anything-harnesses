from setuptools import setup
setup(
    name='cli-anything-coach',
    version='1.0.0',
    packages=['cli_anything.coach'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coach=cli_anything.coach:cli']},
)
