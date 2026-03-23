import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ball running')
@cli.command()
def start(): click.echo('ball started')
if __name__ == '__main__': cli()
