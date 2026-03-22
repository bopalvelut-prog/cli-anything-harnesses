import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Joomla status')
@cli.command()
def extensions(): click.echo('Joomla extensions')
if __name__ == '__main__': cli()
