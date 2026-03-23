from setuptools import setup
setup(
    name='cli-anything-crazyflie',
    version='1.0.0',
    packages=['cli_anything.crazyflie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crazyflie=cli_anything.crazyflie:cli']},
)
