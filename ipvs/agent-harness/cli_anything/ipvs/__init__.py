import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ipvs running')
@cli.command()
def start(): click.echo('ipvs started')
if __name__ == '__main__': cli()
