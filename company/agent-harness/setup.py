from setuptools import setup
setup(
    name='cli-anything-company',
    version='1.0.0',
    packages=['cli_anything.company'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-company=cli_anything.company:cli']},
)
