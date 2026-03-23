from setuptools import setup
setup(
    name='cli-anything-spring_security',
    version='1.0.0',
    packages=['cli_anything.spring_security'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spring_security=cli_anything.spring_security:cli']},
)
