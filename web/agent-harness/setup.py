from setuptools import setup
setup(
    name='cli-anything-web',
    version='1.0.0',
    packages=['cli_anything.web'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-web=cli_anything.web:cli']},
)
