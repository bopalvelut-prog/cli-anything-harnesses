from setuptools import setup
setup(
    name='cli-anything-smoke',
    version='1.0.0',
    packages=['cli_anything.smoke'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smoke=cli_anything.smoke:cli']},
)
