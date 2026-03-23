from setuptools import setup
setup(
    name='cli-anything-pension',
    version='1.0.0',
    packages=['cli_anything.pension'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pension=cli_anything.pension:cli']},
)
