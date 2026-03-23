import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vulcan running')
@cli.command()
def start(): click.echo('vulcan started')
if __name__ == '__main__': cli()
