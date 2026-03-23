import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('binary running')
@cli.command()
def start(): click.echo('binary started')
if __name__ == '__main__': cli()
