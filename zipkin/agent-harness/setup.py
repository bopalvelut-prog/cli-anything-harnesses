from setuptools import setup
setup(
    name='cli-anything-zipkin',
    version='1.0.0',
    packages=['cli_anything.zipkin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zipkin=cli_anything.zipkin:cli']},
)
