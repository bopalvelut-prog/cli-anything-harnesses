from setuptools import setup
setup(
    name='cli-anything-flyway',
    version='1.0.0',
    packages=['cli_anything.flyway'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flyway=cli_anything.flyway:cli']},
)
