import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prison running')
@cli.command()
def start(): click.echo('prison started')
if __name__ == '__main__': cli()
