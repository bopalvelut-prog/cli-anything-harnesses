from setuptools import setup
setup(
    name='cli-anything-career',
    version='1.0.0',
    packages=['cli_anything.career'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-career=cli_anything.career:cli']},
)
