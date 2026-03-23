from setuptools import setup
setup(
    name='cli-anything-mesa',
    version='1.0.0',
    packages=['cli_anything.mesa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mesa=cli_anything.mesa:cli']},
)
