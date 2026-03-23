import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('builder running')
@cli.command()
def start(): click.echo('builder started')
if __name__ == '__main__': cli()
