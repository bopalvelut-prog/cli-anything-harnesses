import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pillar running')
@cli.command()
def start(): click.echo('pillar started')
if __name__ == '__main__': cli()
