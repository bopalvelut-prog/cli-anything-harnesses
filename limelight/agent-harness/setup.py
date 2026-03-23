from setuptools import setup
setup(
    name='cli-anything-limelight',
    version='1.0.0',
    packages=['cli_anything.limelight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-limelight=cli_anything.limelight:cli']},
)
