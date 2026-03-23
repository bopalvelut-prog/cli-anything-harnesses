import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scaler running')
@cli.command()
def start(): click.echo('scaler started')
if __name__ == '__main__': cli()
