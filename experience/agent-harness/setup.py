from setuptools import setup
setup(
    name='cli-anything-experience',
    version='1.0.0',
    packages=['cli_anything.experience'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-experience=cli_anything.experience:cli']},
)
