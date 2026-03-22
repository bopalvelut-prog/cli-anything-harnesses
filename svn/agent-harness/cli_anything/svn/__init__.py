import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def checkout(): click.echo('svn checkout')
@cli.command()
def status(): subprocess.run(['svn', 'status'])
@cli.command()
def commit(): subprocess.run(['svn', 'commit', '-m', 'update'])
if __name__ == '__main__': cli()
