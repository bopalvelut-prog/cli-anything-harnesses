from setuptools import setup
setup(
    name='cli-anything-nscd',
    version='1.0.0',
    packages=['cli_anything.nscd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nscd=cli_anything.nscd:cli']},
)
