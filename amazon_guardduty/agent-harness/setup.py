from setuptools import setup
setup(
    name='cli-anything-amazon_guardduty',
    version='1.0.0',
    packages=['cli_anything.amazon_guardduty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_guardduty=cli_anything.amazon_guardduty:cli']},
)
