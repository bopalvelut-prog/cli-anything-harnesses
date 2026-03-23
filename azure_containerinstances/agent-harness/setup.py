from setuptools import setup
setup(
    name='cli-anything-azure_containerinstances',
    version='1.0.0',
    packages=['cli_anything.azure_containerinstances'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_containerinstances=cli_anything.azure_containerinstances:cli']},
)
