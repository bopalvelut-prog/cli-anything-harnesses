import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shore running')
@cli.command()
def start(): click.echo('shore started')
if __name__ == '__main__': cli()
