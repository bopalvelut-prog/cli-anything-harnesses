from setuptools import setup
setup(
    name='cli-anything-xml',
    version='1.0.0',
    packages=['cli_anything.xml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xml=cli_anything.xml:cli']},
)
