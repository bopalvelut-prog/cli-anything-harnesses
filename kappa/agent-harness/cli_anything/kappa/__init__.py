import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kappa running')
@cli.command()
def start(): click.echo('kappa started')
if __name__ == '__main__': cli()
