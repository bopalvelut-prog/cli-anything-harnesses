from setuptools import setup
setup(
    name='cli-anything-automl',
    version='1.0.0',
    packages=['cli_anything.automl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-automl=cli_anything.automl:cli']},
)
