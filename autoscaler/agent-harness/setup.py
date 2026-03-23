from setuptools import setup
setup(
    name='cli-anything-autoscaler',
    version='1.0.0',
    packages=['cli_anything.autoscaler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autoscaler=cli_anything.autoscaler:cli']},
)
