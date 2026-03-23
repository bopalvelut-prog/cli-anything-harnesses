import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nio running')
@cli.command()
def start(): click.echo('nio started')
if __name__ == '__main__': cli()
