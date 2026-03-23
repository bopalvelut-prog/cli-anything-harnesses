import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('automate running')
@cli.command()
def start(): click.echo('automate started')
if __name__ == '__main__': cli()
