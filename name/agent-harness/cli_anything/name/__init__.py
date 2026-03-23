import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('name running')
@cli.command()
def start(): click.echo('name started')
if __name__ == '__main__': cli()
