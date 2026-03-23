from setuptools import setup
setup(
    name='cli-anything-gatling',
    version='1.0.0',
    packages=['cli_anything.gatling'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gatling=cli_anything.gatling:cli']},
)
