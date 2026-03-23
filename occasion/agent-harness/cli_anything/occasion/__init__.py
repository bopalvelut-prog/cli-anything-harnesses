import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('occasion running')
@cli.command()
def start(): click.echo('occasion started')
if __name__ == '__main__': cli()
