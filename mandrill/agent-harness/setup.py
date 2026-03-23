from setuptools import setup
setup(
    name='cli-anything-mandrill',
    version='1.0.0',
    packages=['cli_anything.mandrill'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mandrill=cli_anything.mandrill:cli']},
)
