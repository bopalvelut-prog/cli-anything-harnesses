from setuptools import setup
setup(
    name='cli-anything-devdocs',
    version='1.0.0',
    packages=['cli_anything.devdocs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-devdocs=cli_anything.devdocs:cli']},
)
