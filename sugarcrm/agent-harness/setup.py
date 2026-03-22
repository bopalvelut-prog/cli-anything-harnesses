from setuptools import setup
setup(
    name='cli-anything-sugarcrm',
    version='1.0.0',
    packages=['cli_anything.sugarcrm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sugarcrm=cli_anything.sugarcrm:cli']},
)
