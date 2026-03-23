from setuptools import setup
setup(
    name='cli-anything-transportation',
    version='1.0.0',
    packages=['cli_anything.transportation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transportation=cli_anything.transportation:cli']},
)
