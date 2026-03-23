from setuptools import setup
setup(
    name='cli-anything-distcp',
    version='1.0.0',
    packages=['cli_anything.distcp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-distcp=cli_anything.distcp:cli']},
)
