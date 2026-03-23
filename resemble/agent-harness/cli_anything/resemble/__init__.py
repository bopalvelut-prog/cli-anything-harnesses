import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resemble running')
@cli.command()
def start(): click.echo('resemble started')
if __name__ == '__main__': cli()
