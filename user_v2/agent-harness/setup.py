from setuptools import setup
setup(
    name='cli-anything-user_v2',
    version='1.0.0',
    packages=['cli_anything.user_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-user_v2=cli_anything.user_v2:cli']},
)
