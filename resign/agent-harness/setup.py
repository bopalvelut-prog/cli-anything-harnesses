from setuptools import setup
setup(
    name='cli-anything-resign',
    version='1.0.0',
    packages=['cli_anything.resign'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resign=cli_anything.resign:cli']},
)
