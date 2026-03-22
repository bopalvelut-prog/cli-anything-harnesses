from setuptools import setup
setup(
    name='cli-anything-drawio_online',
    version='1.0.0',
    packages=['cli_anything.drawio_online'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drawio_online=cli_anything.drawio_online:cli']},
)
