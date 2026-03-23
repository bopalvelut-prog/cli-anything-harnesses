import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ldaps running')
@cli.command()
def start(): click.echo('ldaps started')
if __name__ == '__main__': cli()
