import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def clone(): click.echo('hg clone')
@cli.command()
def status(): subprocess.run(['hg', 'status'])
@cli.command()
def commit(): subprocess.run(['hg', 'commit'])
if __name__ == '__main__': cli()
