import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('table running')
@cli.command()
def start(): click.echo('table started')
if __name__ == '__main__': cli()
