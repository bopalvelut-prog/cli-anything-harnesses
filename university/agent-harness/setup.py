from setuptools import setup
setup(
    name='cli-anything-university',
    version='1.0.0',
    packages=['cli_anything.university'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-university=cli_anything.university:cli']},
)
