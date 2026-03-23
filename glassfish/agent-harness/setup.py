from setuptools import setup
setup(
    name='cli-anything-glassfish',
    version='1.0.0',
    packages=['cli_anything.glassfish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glassfish=cli_anything.glassfish:cli']},
)
