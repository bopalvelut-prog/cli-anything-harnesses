from setuptools import setup
setup(
    name='cli-anything-giant',
    version='1.0.0',
    packages=['cli_anything.giant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-giant=cli_anything.giant:cli']},
)
