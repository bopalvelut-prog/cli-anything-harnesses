from setuptools import setup
setup(
    name='cli-anything-resource',
    version='1.0.0',
    packages=['cli_anything.resource'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resource=cli_anything.resource:cli']},
)
