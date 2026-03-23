import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('antmedia running')
@cli.command()
def start(): click.echo('antmedia started')
if __name__ == '__main__': cli()
