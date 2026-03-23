from setuptools import setup
setup(
    name='cli-anything-posthog',
    version='1.0.0',
    packages=['cli_anything.posthog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-posthog=cli_anything.posthog:cli']},
)
