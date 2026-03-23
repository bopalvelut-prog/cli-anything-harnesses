from setuptools import setup
setup(
    name='cli-anything-calibreweb',
    version='1.0.0',
    packages=['cli_anything.calibreweb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-calibreweb=cli_anything.calibreweb:cli']},
)
