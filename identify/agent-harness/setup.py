from setuptools import setup
setup(
    name='cli-anything-identify',
    version='1.0.0',
    packages=['cli_anything.identify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-identify=cli_anything.identify:cli']},
)
