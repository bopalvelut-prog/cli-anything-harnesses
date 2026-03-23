from setuptools import setup
setup(
    name='cli-anything-serve',
    version='1.0.0',
    packages=['cli_anything.serve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-serve=cli_anything.serve:cli']},
)
