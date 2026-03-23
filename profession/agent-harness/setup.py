from setuptools import setup
setup(
    name='cli-anything-profession',
    version='1.0.0',
    packages=['cli_anything.profession'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-profession=cli_anything.profession:cli']},
)
