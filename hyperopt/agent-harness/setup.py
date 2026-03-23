from setuptools import setup
setup(
    name='cli-anything-hyperopt',
    version='1.0.0',
    packages=['cli_anything.hyperopt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hyperopt=cli_anything.hyperopt:cli']},
)
