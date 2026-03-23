import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unhappy running')
@cli.command()
def start(): click.echo('unhappy started')
if __name__ == '__main__': cli()
