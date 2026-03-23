import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crime running')
@cli.command()
def start(): click.echo('crime started')
if __name__ == '__main__': cli()
