from setuptools import setup
setup(
    name='cli-anything-ripple',
    version='1.0.0',
    packages=['cli_anything.ripple'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ripple=cli_anything.ripple:cli']},
)
