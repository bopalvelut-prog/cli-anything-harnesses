from setuptools import setup
setup(
    name='cli-anything-aws_waf',
    version='1.0.0',
    packages=['cli_anything.aws_waf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_waf=cli_anything.aws_waf:cli']},
)
