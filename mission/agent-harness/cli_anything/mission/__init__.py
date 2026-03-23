import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mission running')
@cli.command()
def start(): click.echo('mission started')
if __name__ == '__main__': cli()
