import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apache_eagle running')
@cli.command()
def start(): click.echo('apache_eagle started')
if __name__ == '__main__': cli()
