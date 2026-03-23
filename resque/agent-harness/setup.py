from setuptools import setup
setup(
    name='cli-anything-resque',
    version='1.0.0',
    packages=['cli_anything.resque'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resque=cli_anything.resque:cli']},
)
