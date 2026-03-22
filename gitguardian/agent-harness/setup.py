from setuptools import setup
setup(
    name='cli-anything-gitguardian',
    version='1.0.0',
    packages=['cli_anything.gitguardian'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gitguardian=cli_anything.gitguardian:cli']},
)
