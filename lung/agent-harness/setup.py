from setuptools import setup
setup(
    name='cli-anything-lung',
    version='1.0.0',
    packages=['cli_anything.lung'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lung=cli_anything.lung:cli']},
)
