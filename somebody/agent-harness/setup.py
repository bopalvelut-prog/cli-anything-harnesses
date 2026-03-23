from setuptools import setup
setup(
    name='cli-anything-somebody',
    version='1.0.0',
    packages=['cli_anything.somebody'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-somebody=cli_anything.somebody:cli']},
)
