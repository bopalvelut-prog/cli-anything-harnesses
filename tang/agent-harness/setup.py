from setuptools import setup
setup(
    name='cli-anything-tang',
    version='1.0.0',
    packages=['cli_anything.tang'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tang=cli_anything.tang:cli']},
)
