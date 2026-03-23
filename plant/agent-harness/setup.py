from setuptools import setup
setup(
    name='cli-anything-plant',
    version='1.0.0',
    packages=['cli_anything.plant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plant=cli_anything.plant:cli']},
)
