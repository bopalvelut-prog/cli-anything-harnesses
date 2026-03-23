import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('timeline running')
@cli.command()
def start(): click.echo('timeline started')
if __name__ == '__main__': cli()
