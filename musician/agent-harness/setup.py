from setuptools import setup
setup(
    name='cli-anything-musician',
    version='1.0.0',
    packages=['cli_anything.musician'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-musician=cli_anything.musician:cli']},
)
