from setuptools import setup
setup(
    name='cli-anything-publish',
    version='1.0.0',
    packages=['cli_anything.publish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-publish=cli_anything.publish:cli']},
)
