from setuptools import setup
setup(
    name='cli-anything-bcrypt',
    version='1.0.0',
    packages=['cli_anything.bcrypt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bcrypt=cli_anything.bcrypt:cli']},
)
