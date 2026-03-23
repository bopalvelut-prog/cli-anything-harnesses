from setuptools import setup
setup(
    name='cli-anything-ant',
    version='1.0.0',
    packages=['cli_anything.ant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ant=cli_anything.ant:cli']},
)
