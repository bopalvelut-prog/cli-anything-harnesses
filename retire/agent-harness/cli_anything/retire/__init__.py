import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('retire running')
@cli.command()
def start(): click.echo('retire started')
if __name__ == '__main__': cli()
