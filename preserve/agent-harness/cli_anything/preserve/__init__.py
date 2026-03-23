import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('preserve running')
@cli.command()
def start(): click.echo('preserve started')
if __name__ == '__main__': cli()
