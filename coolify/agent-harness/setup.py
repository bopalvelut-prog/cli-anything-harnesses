from setuptools import setup
setup(
    name='cli-anything-coolify',
    version='1.0.0',
    packages=['cli_anything.coolify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coolify=cli_anything.coolify:cli']},
)
