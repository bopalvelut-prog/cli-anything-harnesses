from setuptools import setup
setup(
    name='cli-anything-seriously',
    version='1.0.0',
    packages=['cli_anything.seriously'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seriously=cli_anything.seriously:cli']},
)
