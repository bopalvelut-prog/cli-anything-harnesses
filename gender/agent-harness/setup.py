from setuptools import setup
setup(
    name='cli-anything-gender',
    version='1.0.0',
    packages=['cli_anything.gender'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gender=cli_anything.gender:cli']},
)
