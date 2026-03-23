import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apache_ranger running')
@cli.command()
def start(): click.echo('apache_ranger started')
if __name__ == '__main__': cli()
