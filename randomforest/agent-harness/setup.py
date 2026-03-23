from setuptools import setup
setup(
    name='cli-anything-randomforest',
    version='1.0.0',
    packages=['cli_anything.randomforest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-randomforest=cli_anything.randomforest:cli']},
)
