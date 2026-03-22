from setuptools import setup
setup(
    name='cli-anything-supervisor',
    version='1.0.0',
    packages=['cli_anything.supervisor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-supervisor=cli_anything.supervisor:cli']},
)
