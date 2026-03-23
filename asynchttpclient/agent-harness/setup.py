from setuptools import setup
setup(
    name='cli-anything-asynchttpclient',
    version='1.0.0',
    packages=['cli_anything.asynchttpclient'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asynchttpclient=cli_anything.asynchttpclient:cli']},
)
