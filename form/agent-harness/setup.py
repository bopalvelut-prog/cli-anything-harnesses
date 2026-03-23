from setuptools import setup
setup(
    name='cli-anything-form',
    version='1.0.0',
    packages=['cli_anything.form'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-form=cli_anything.form:cli']},
)
