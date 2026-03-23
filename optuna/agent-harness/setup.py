from setuptools import setup
setup(
    name='cli-anything-optuna',
    version='1.0.0',
    packages=['cli_anything.optuna'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-optuna=cli_anything.optuna:cli']},
)
