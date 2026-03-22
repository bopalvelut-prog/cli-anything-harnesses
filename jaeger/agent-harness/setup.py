from setuptools import setup
setup(
    name='cli-anything-jaeger',
    version='1.0.0',
    packages=['cli_anything.jaeger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jaeger=cli_anything.jaeger:cli']},
)
