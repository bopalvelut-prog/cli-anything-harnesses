import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rush running')
@cli.command()
def start(): click.echo('rush started')
if __name__ == '__main__': cli()
