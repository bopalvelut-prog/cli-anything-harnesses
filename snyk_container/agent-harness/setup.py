from setuptools import setup
setup(
    name='cli-anything-snyk_container',
    version='1.0.0',
    packages=['cli_anything.snyk_container'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-snyk_container=cli_anything.snyk_container:cli']},
)
