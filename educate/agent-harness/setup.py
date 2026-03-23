from setuptools import setup
setup(
    name='cli-anything-educate',
    version='1.0.0',
    packages=['cli_anything.educate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-educate=cli_anything.educate:cli']},
)
