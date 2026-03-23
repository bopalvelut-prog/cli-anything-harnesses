from setuptools import setup
setup(
    name='cli-anything-apiman',
    version='1.0.0',
    packages=['cli_anything.apiman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apiman=cli_anything.apiman:cli']},
)
