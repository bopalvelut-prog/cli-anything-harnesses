from setuptools import setup
setup(
    name='cli-anything-axum',
    version='1.0.0',
    packages=['cli_anything.axum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-axum=cli_anything.axum:cli']},
)
