import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['sentry-cli', 'login'])
@cli.command()
def upload(): subprocess.run(['sentry-cli', 'upload-dif'])
@cli.command()
def releases(): subprocess.run(['sentry-cli', 'releases', 'list'])
if __name__ == '__main__': cli()
