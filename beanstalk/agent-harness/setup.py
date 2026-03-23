from setuptools import setup
setup(
    name='cli-anything-beanstalk',
    version='1.0.0',
    packages=['cli_anything.beanstalk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beanstalk=cli_anything.beanstalk:cli']},
)
