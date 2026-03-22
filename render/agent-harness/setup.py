from setuptools import setup
setup(
    name='cli-anything-render',
    version='1.0.0',
    packages=['cli_anything.render'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-render=cli_anything.render:cli']},
)
