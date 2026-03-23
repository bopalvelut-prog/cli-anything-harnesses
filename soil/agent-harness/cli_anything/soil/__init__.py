import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('soil running')
@cli.command()
def start(): click.echo('soil started')
if __name__ == '__main__': cli()
