from setuptools import setup
setup(
    name='cli-anything-circuit_breaker',
    version='1.0.0',
    packages=['cli_anything.circuit_breaker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-circuit_breaker=cli_anything.circuit_breaker:cli']},
)
