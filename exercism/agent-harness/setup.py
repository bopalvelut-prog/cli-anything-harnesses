from setuptools import setup
setup(
    name='cli-anything-exercism',
    version='1.0.0',
    packages=['cli_anything.exercism'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exercism=cli_anything.exercism:cli']},
)
