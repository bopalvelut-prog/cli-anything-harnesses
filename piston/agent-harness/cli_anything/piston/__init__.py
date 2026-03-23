import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('piston running')
@cli.command()
def start(): click.echo('piston started')
if __name__ == '__main__': cli()
