from setuptools import setup
setup(
    name='cli-anything-mockito',
    version='1.0.0',
    packages=['cli_anything.mockito'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mockito=cli_anything.mockito:cli']},
)
