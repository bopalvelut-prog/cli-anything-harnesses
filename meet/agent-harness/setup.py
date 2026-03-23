from setuptools import setup
setup(
    name='cli-anything-meet',
    version='1.0.0',
    packages=['cli_anything.meet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meet=cli_anything.meet:cli']},
)
