from setuptools import setup
setup(
    name='cli-anything-duty',
    version='1.0.0',
    packages=['cli_anything.duty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-duty=cli_anything.duty:cli']},
)
