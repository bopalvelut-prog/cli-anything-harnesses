from setuptools import setup
setup(
    name='cli-anything-joint',
    version='1.0.0',
    packages=['cli_anything.joint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-joint=cli_anything.joint:cli']},
)
