from setuptools import setup
setup(
    name='cli-anything-locust',
    version='1.0.0',
    packages=['cli_anything.locust'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-locust=cli_anything.locust:cli']},
)
