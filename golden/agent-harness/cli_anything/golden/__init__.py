import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('golden running')
@cli.command()
def start(): click.echo('golden started')
if __name__ == '__main__': cli()
