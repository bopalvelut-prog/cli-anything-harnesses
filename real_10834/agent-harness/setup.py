from setuptools import setup
setup(
    name='cli-anything-real_10834',
    version='1.0.0',
    packages=['cli_anything.real_10834'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_10834=cli_anything.real_10834:cli']},
)
