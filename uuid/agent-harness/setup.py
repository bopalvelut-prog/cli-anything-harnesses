from setuptools import setup
setup(
    name='cli-anything-uuid',
    version='1.0.0',
    packages=['cli_anything.uuid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uuid=cli_anything.uuid:cli']},
)
