import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('global running')
@cli.command()
def start(): click.echo('global started')
if __name__ == '__main__': cli()
