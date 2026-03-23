import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('same running')
@cli.command()
def start(): click.echo('same started')
if __name__ == '__main__': cli()
