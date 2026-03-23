import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('restart running')
@cli.command()
def start(): click.echo('restart started')
if __name__ == '__main__': cli()
