from setuptools import setup
setup(
    name='cli-anything-toward',
    version='1.0.0',
    packages=['cli_anything.toward'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toward=cli_anything.toward:cli']},
)
