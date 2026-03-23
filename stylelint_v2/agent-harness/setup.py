from setuptools import setup
setup(
    name='cli-anything-stylelint_v2',
    version='1.0.0',
    packages=['cli_anything.stylelint_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stylelint_v2=cli_anything.stylelint_v2:cli']},
)
