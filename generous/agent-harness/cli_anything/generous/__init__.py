import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('generous running')
@cli.command()
def start(): click.echo('generous started')
if __name__ == '__main__': cli()
