from setuptools import setup
setup(
    name='cli-anything-scaler',
    version='1.0.0',
    packages=['cli_anything.scaler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scaler=cli_anything.scaler:cli']},
)
