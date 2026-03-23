import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('arctic running')
@cli.command()
def start(): click.echo('arctic started')
if __name__ == '__main__': cli()
