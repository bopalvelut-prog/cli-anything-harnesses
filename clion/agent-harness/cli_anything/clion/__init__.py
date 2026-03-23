import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clion running')
@cli.command()
def start(): click.echo('clion started')
if __name__ == '__main__': cli()
