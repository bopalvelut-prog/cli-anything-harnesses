from setuptools import setup
setup(
    name='cli-anything-wild',
    version='1.0.0',
    packages=['cli_anything.wild'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wild=cli_anything.wild:cli']},
)
