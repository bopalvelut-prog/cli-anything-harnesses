from setuptools import setup
setup(
    name='cli-anything-azure_blueprint',
    version='1.0.0',
    packages=['cli_anything.azure_blueprint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_blueprint=cli_anything.azure_blueprint:cli']},
)
