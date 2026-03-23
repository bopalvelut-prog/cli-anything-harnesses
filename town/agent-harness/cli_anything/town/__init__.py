import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('town running')
@cli.command()
def start(): click.echo('town started')
if __name__ == '__main__': cli()
