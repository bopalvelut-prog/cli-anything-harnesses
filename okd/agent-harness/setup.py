from setuptools import setup
setup(
    name='cli-anything-okd',
    version='1.0.0',
    packages=['cli_anything.okd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-okd=cli_anything.okd:cli']},
)
