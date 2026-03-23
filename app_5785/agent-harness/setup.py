from setuptools import setup
setup(
    name='cli-anything-app_5785',
    version='1.0.0',
    packages=['cli_anything.app_5785'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5785=cli_anything.app_5785:cli']},
)
