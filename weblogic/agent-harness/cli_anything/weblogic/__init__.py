import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weblogic running')
@cli.command()
def start(): click.echo('weblogic started')
if __name__ == '__main__': cli()
