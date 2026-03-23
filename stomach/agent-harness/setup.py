from setuptools import setup
setup(
    name='cli-anything-stomach',
    version='1.0.0',
    packages=['cli_anything.stomach'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stomach=cli_anything.stomach:cli']},
)
