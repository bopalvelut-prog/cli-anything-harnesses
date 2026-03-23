from setuptools import setup
setup(
    name='cli-anything-beanstalkd',
    version='1.0.0',
    packages=['cli_anything.beanstalkd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beanstalkd=cli_anything.beanstalkd:cli']},
)
