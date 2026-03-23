from setuptools import setup
setup(
    name='cli-anything-plantuml',
    version='1.0.0',
    packages=['cli_anything.plantuml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plantuml=cli_anything.plantuml:cli']},
)
