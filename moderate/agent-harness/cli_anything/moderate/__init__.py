import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('moderate running')
@cli.command()
def start(): click.echo('moderate started')
if __name__ == '__main__': cli()
