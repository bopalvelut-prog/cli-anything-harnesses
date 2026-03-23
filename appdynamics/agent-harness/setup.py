from setuptools import setup
setup(
    name='cli-anything-appdynamics',
    version='1.0.0',
    packages=['cli_anything.appdynamics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appdynamics=cli_anything.appdynamics:cli']},
)
