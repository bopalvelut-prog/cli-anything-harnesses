from setuptools import setup
setup(
    name='cli-anything-kappa',
    version='1.0.0',
    packages=['cli_anything.kappa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kappa=cli_anything.kappa:cli']},
)
