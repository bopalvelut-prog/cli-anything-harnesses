from setuptools import setup
setup(
    name='cli-anything-disease',
    version='1.0.0',
    packages=['cli_anything.disease'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-disease=cli_anything.disease:cli']},
)
