from setuptools import setup
setup(
    name='cli-anything-marriage',
    version='1.0.0',
    packages=['cli_anything.marriage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-marriage=cli_anything.marriage:cli']},
)
