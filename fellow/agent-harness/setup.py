from setuptools import setup
setup(
    name='cli-anything-fellow',
    version='1.0.0',
    packages=['cli_anything.fellow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fellow=cli_anything.fellow:cli']},
)
