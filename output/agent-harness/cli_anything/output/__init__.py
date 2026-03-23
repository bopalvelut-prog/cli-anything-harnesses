import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('output running')
@cli.command()
def start(): click.echo('output started')
if __name__ == '__main__': cli()
