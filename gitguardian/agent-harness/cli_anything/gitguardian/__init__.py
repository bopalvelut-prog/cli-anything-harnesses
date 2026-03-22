import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['ggshield', 'secret', 'scan', 'path', '.'])
@cli.command()
def status(): click.echo('GitGuardian status')
if __name__ == '__main__': cli()
