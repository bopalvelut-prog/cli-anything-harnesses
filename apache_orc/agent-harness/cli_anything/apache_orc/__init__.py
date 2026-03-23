import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apache_orc running')
@cli.command()
def start(): click.echo('apache_orc started')
if __name__ == '__main__': cli()
