from setuptools import setup
setup(
    name='cli-anything-inspectit',
    version='1.0.0',
    packages=['cli_anything.inspectit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inspectit=cli_anything.inspectit:cli']},
)
