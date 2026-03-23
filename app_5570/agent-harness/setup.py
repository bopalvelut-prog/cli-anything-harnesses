from setuptools import setup
setup(
    name='cli-anything-app_5570',
    version='1.0.0',
    packages=['cli_anything.app_5570'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5570=cli_anything.app_5570:cli']},
)
