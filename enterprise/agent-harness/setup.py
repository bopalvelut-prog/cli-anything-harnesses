from setuptools import setup
setup(
    name='cli-anything-enterprise',
    version='1.0.0',
    packages=['cli_anything.enterprise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-enterprise=cli_anything.enterprise:cli']},
)
