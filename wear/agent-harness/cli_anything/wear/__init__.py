import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wear running')
@cli.command()
def start(): click.echo('wear started')
if __name__ == '__main__': cli()
