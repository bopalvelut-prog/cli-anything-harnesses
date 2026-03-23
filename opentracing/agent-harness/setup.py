from setuptools import setup
setup(
    name='cli-anything-opentracing',
    version='1.0.0',
    packages=['cli_anything.opentracing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opentracing=cli_anything.opentracing:cli']},
)
