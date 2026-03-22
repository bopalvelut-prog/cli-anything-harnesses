import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def register(): subprocess.run(['acme.sh', '--register-account'])
@cli.command()
@click.argument('domain')
def issue(domain): subprocess.run(['acme.sh', '--issue', '-d', domain])
if __name__ == '__main__': cli()
