import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('darkmode running')
@cli.command()
def start(): click.echo('darkmode started')
if __name__ == '__main__': cli()
