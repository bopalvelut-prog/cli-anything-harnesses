from setuptools import setup
setup(
    name='cli-anything-jmeter',
    version='1.0.0',
    packages=['cli_anything.jmeter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jmeter=cli_anything.jmeter:cli']},
)
