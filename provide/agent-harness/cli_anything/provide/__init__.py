import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('provide running')
@cli.command()
def start(): click.echo('provide started')
if __name__ == '__main__': cli()
