import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('report running')
@cli.command()
def start(): click.echo('report started')
if __name__ == '__main__': cli()
