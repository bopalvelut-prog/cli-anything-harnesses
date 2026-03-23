import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('assignment running')
@cli.command()
def start(): click.echo('assignment started')
if __name__ == '__main__': cli()
