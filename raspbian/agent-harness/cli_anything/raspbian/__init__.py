import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('raspbian running')
@cli.command()
def start(): click.echo('raspbian started')
if __name__ == '__main__': cli()
