from setuptools import setup
setup(
    name='cli-anything-real_app_1174',
    version='1.0.0',
    packages=['cli_anything.real_app_1174'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_1174=cli_anything.real_app_1174:cli']},
)
