import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('meal running')
@cli.command()
def start(): click.echo('meal started')
if __name__ == '__main__': cli()
