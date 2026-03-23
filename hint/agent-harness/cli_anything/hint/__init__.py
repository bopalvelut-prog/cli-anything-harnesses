import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hint running')
@cli.command()
def start(): click.echo('hint started')
if __name__ == '__main__': cli()
