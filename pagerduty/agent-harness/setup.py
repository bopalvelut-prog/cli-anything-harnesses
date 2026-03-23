from setuptools import setup
setup(
    name='cli-anything-pagerduty',
    version='1.0.0',
    packages=['cli_anything.pagerduty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pagerduty=cli_anything.pagerduty:cli']},
)
