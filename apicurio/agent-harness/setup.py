from setuptools import setup
setup(
    name='cli-anything-apicurio',
    version='1.0.0',
    packages=['cli_anything.apicurio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apicurio=cli_anything.apicurio:cli']},
)
