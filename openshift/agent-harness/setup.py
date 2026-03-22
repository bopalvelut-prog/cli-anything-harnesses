from setuptools import setup
setup(
    name='cli-anything-openshift',
    version='1.0.0',
    packages=['cli_anything.openshift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openshift=cli_anything.openshift:cli']},
)
