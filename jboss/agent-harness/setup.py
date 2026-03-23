from setuptools import setup
setup(
    name='cli-anything-jboss',
    version='1.0.0',
    packages=['cli_anything.jboss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jboss=cli_anything.jboss:cli']},
)
