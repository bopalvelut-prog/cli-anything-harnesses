from setuptools import setup
setup(
    name='cli-anything-xgboost',
    version='1.0.0',
    packages=['cli_anything.xgboost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xgboost=cli_anything.xgboost:cli']},
)
