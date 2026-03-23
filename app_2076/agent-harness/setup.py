from setuptools import setup
setup(
    name='cli-anything-app_2076',
    version='1.0.0',
    packages=['cli_anything.app_2076'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_2076=cli_anything.app_2076:cli']},
)
