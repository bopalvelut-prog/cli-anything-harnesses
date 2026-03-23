from setuptools import setup
setup(
    name='cli-anything-turtle',
    version='1.0.0',
    packages=['cli_anything.turtle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-turtle=cli_anything.turtle:cli']},
)
