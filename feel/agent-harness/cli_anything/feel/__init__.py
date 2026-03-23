import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('feel running')
@cli.command()
def start(): click.echo('feel started')
if __name__ == '__main__': cli()
