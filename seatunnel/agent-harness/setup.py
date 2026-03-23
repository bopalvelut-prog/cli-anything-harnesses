from setuptools import setup
setup(
    name='cli-anything-seatunnel',
    version='1.0.0',
    packages=['cli_anything.seatunnel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seatunnel=cli_anything.seatunnel:cli']},
)
