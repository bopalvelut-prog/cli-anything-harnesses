import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apache_jena running')
@cli.command()
def start(): click.echo('apache_jena started')
if __name__ == '__main__': cli()
