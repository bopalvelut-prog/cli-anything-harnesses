from setuptools import setup
setup(
    name='cli-anything-woman',
    version='1.0.0',
    packages=['cli_anything.woman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-woman=cli_anything.woman:cli']},
)
