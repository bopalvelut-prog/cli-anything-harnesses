import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('operator running')
@cli.command()
def start(): click.echo('operator started')
if __name__ == '__main__': cli()
