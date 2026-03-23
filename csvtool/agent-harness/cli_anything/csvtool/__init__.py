import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('csvtool running')
@cli.command()
def start(): click.echo('csvtool started')
if __name__ == '__main__': cli()
