from setuptools import setup
setup(
    name='cli-anything-birth',
    version='1.0.0',
    packages=['cli_anything.birth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-birth=cli_anything.birth:cli']},
)
