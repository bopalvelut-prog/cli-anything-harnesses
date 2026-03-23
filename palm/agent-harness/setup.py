from setuptools import setup
setup(
    name='cli-anything-palm',
    version='1.0.0',
    packages=['cli_anything.palm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-palm=cli_anything.palm:cli']},
)
