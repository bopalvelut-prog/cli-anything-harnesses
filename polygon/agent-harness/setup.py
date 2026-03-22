from setuptools import setup
setup(
    name='cli-anything-polygon',
    version='1.0.0',
    packages=['cli_anything.polygon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-polygon=cli_anything.polygon:cli']},
)
