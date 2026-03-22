from setuptools import setup
setup(
    name='cli-anything-sparkpost',
    version='1.0.0',
    packages=['cli_anything.sparkpost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sparkpost=cli_anything.sparkpost:cli']},
)
