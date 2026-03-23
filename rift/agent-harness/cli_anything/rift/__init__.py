import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rift running')
@cli.command()
def start(): click.echo('rift started')
if __name__ == '__main__': cli()
