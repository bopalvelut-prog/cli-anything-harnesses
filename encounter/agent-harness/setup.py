from setuptools import setup
setup(
    name='cli-anything-encounter',
    version='1.0.0',
    packages=['cli_anything.encounter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-encounter=cli_anything.encounter:cli']},
)
