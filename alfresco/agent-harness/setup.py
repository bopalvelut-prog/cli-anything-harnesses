from setuptools import setup
setup(
    name='cli-anything-alfresco',
    version='1.0.0',
    packages=['cli_anything.alfresco'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alfresco=cli_anything.alfresco:cli']},
)
