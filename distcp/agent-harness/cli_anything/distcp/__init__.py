import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('distcp running')
@cli.command()
def start(): click.echo('distcp started')
if __name__ == '__main__': cli()
