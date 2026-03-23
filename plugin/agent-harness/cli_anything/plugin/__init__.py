import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plugin running')
@cli.command()
def start(): click.echo('plugin started')
if __name__ == '__main__': cli()
