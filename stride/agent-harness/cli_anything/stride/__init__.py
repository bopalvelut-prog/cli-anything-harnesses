import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stride running')
@cli.command()
def start(): click.echo('stride started')
if __name__ == '__main__': cli()
