import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('carbon running')
@cli.command()
def start(): click.echo('carbon started')
if __name__ == '__main__': cli()
