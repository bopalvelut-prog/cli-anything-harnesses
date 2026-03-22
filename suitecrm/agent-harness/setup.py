from setuptools import setup
setup(
    name='cli-anything-suitecrm',
    version='1.0.0',
    packages=['cli_anything.suitecrm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suitecrm=cli_anything.suitecrm:cli']},
)
