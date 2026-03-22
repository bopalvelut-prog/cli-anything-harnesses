from setuptools import setup
setup(
    name='cli-anything-acronis',
    version='1.0.0',
    packages=['cli_anything.acronis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-acronis=cli_anything.acronis:cli']},
)
