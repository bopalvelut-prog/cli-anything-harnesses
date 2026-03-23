import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mechanize running')
@cli.command()
def start(): click.echo('mechanize started')
if __name__ == '__main__': cli()
